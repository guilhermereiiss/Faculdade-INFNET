from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from sqlmodel import Session
from jose import JWTError
from auth.security import decodificar_token
from database.db import get_session, obter_usuario, obter_evento
from models.usuario import Usuario
from models.evento import Evento

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
    scopes={
        "eventos:read":   "Leitura de eventos",
        "eventos:write":  "Criação e edição de eventos",
        "eventos:delete": "Remoção de eventos",
        "admin:all":      "Acesso administrativo completo",
    },
)


def get_usuario_atual(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> Usuario:
    """
    Exercício 4 — Middleware JWT via dependency injection.
    Valida o token e verifica os escopos necessários antes de qualquer rota sensível.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas ou token expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decodificar_token(token)
        username: str = payload.get("sub")
        token_scopes: list[str] = payload.get("scope", "").split()
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    usuario = obter_usuario(session, username)
    if not usuario:
        raise credentials_exception

    # Verifica cada escopo exigido pela rota
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Escopo insuficiente: '{scope}' necessário",
                headers={"WWW-Authenticate": f'Bearer scope="{security_scopes.scope_str}"'},
            )
    return usuario


def verificar_ownership(evento_id: int, usuario: Usuario, session: Session) -> Evento:
    """
    Exercício 3 & 4 — verifica que o usuário é dono do evento.
    Admin pode acessar qualquer evento; demais usuários apenas os seus.
    """
    evento = obter_evento(session, evento_id)
    if not evento:
        raise HTTPException(status_code=404, detail="Evento não encontrado")

    if usuario.papel == "admin":
        return evento

    if evento.owner_username != usuario.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Você não é o organizador deste evento",
        )
    return evento


def verificar_ownership_inscricao(inscricao, usuario: Usuario) -> None:
    """
    Exercício 3 & 4 — verifica ownership para inscrições.
    Bloqueia acesso a inscrição de outro usuário (BOLA fix).
    """
    if usuario.papel == "admin":
        return
    if inscricao.owner_username != usuario.username:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado: esta inscrição pertence a outro usuário",
        )
