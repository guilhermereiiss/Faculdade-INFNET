from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from jose import JWTError
from auth.security import decodificar_token
import database.db as db
from models.usuario import UsuarioDB
from models.evento import EventoInterno

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
) -> UsuarioDB:
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

    usuario = db.obter_usuario(username)
    if not usuario:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Escopo insuficiente: '{scope}' necessário",
                headers={"WWW-Authenticate": f'Bearer scope="{security_scopes.scope_str}"'},
            )
    return usuario


def verificar_ownership(evento_id: int, usuario: UsuarioDB) -> EventoInterno:
    evento = db.obter_evento(evento_id)
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
