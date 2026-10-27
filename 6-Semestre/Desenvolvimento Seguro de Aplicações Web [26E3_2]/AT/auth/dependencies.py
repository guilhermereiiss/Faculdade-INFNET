from typing import Optional, List
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from sqlmodel import Session
from jose import JWTError
from auth.security import decodificar_token, SCOPES_POR_PAPEL
from database.db import (
    get_session,
    obter_usuario_por_username,
    obter_consulta_por_id,
    obter_profissional_por_id,
    obter_profissional_por_username,
)
from models.usuario import Usuario
from models.consulta import Consulta

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
    scopes={
        "consultas:read": "Leitura de consultas",
        "consultas:write": "Criação e edição de consultas",
        "consultas:delete": "Cancelamento e remoção de consultas",
        "pacientes:read": "Leitura de dados cadastrais de pacientes",
        "pacientes:write": "Cadastro e atualização de pacientes",
        "pacientes:delete": "Remoção de registros de pacientes",
        "profissionais:read": "Leitura de dados de profissionais",
        "profissionais:write": "Cadastro de profissionais",
        "prontuario:read": "Acesso a prontuários e diagnósticos sensíveis",
        "prontuario:write": "Evolução clínica e anotação em prontuário",
        "recepcao:agenda": "Acesso à visualização da agenda da recepção",
        "admin:all": "Acesso irrestrito a configurações e auditoria",
        "laboratorio:disponibilidade": "Consulta M2M de horários vagos",
        "laboratorio:exames": "Integração M2M de exames laboratoriais",
    },
)


def get_usuario_atual(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
) -> Usuario:
    """
    Exercício 6 — Middleware de autenticação JWT via Dependency Injection.
    Valida token, expiração, assinatura e verifica escopos exigidos pelo endpoint.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais inválidas, token expirado ou malformado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decodificar_token(token)
        username: Optional[str] = payload.get("sub")
        if not username:
            raise credentials_exception
        token_scopes: List[str] = payload.get("scope", "").split()
        mfa_verified: bool = payload.get("mfa_verified", False)
    except JWTError:
        raise credentials_exception

    usuario = obter_usuario_por_username(session, username)
    if not usuario or not usuario.is_active:
        raise credentials_exception

    # Se for usuário administrativo, exige flag de MFA verificado (Exercício 6)
    if usuario.papel == "admin" and not mfa_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Autenticação multifator (MFA) obrigatória para contas administrativas",
            headers={"WWW-Authenticate": "Bearer error=\"mfa_required\""},
        )

    # Verificação de Escopos OAuth 2.0
    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Escopo insuficiente: '{scope}' é exigido para esta operação",
                headers={"WWW-Authenticate": f'Bearer scope="{security_scopes.scope_str}"'},
            )

    return usuario


def exigir_admin(
    usuario: Usuario = Depends(get_usuario_atual),
) -> Usuario:
    """
    Garante acesso estritamente restrito a administradores com MFA ativo (Exercício 6).
    Retorna 403 Forbidden para qualquer outro papel.
    """
    if usuario.papel != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado: privilégios de administrador requeridos",
        )
    return usuario


def exigir_profissional(
    usuario: Usuario = Depends(get_usuario_atual),
) -> Usuario:
    """
    Exige papel de profissional de saúde ou administrador.
    """
    if usuario.papel not in ["profissional_saude", "admin"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado: restrito a profissionais de saúde e administradores",
        )
    return usuario


def verificar_m2m_laboratorio(
    security_scopes: SecurityScopes,
    token: str = Depends(oauth2_scheme),
) -> dict:
    """
    Exercício 7 — Validação de token M2M para o laboratório parceiro.
    Verifica se o token foi emitido via Client Credentials para a identidade 'm2m:laboratorio'.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token M2M inválido ou expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decodificar_token(token)
        sub: str = payload.get("sub", "")
        papel: str = payload.get("papel", "")
        token_scopes: List[str] = payload.get("scope", "").split()

        if sub != "m2m:laboratorio" or papel != "m2m_laboratorio":
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    for scope in security_scopes.scopes:
        if scope not in token_scopes:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Escopo M2M insuficiente: '{scope}' necessário",
            )
    return payload


def verificar_ownership_consulta(
    consulta_id: int,
    usuario: Usuario,
    session: Session,
    bloquear_recepcao_prontuario: bool = False,
) -> Consulta:
    """
    Exercício 6, 8 e 9 — Prevenção e correção de BOLA (Broken Object Level Authorization).
    Garante que:
    1. Administradores podem acessar qualquer consulta.
    2. Profissionais de saúde APENAS podem acessar e manipular consultas de seus PRÓPRIOS pacientes.
    3. Tentativas de acessar consultas de outro médico resultam em HTTP 403 Forbidden.
    """
    consulta = obter_consulta_por_id(session, consulta_id)
    if not consulta:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Consulta médica não encontrada",
        )

    if usuario.papel == "admin":
        return consulta

    if usuario.papel == "profissional_saude":
        # Localiza o profissional correspondente ao usuário logado
        profissional_logado = obter_profissional_por_username(session, usuario.username)
        if not profissional_logado or consulta.profissional_id != profissional_logado.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Acesso negado: você não é o profissional de saúde responsável por esta consulta",
            )
        return consulta

    if usuario.papel == "recepcionista":
        if bloquear_recepcao_prontuario:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Acesso negado: recepcionistas não têm permissão para acessar prontuários médicos",
            )
        return consulta

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Acesso não autorizado a este recurso",
    )
