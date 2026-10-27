import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

from main import app
from database.db import get_session, seed
from auth.security import criar_token, SCOPES_POR_PAPEL


@pytest.fixture(name="session")
def session_fixture():
    """
    Cria um banco de dados SQLite isolado em memória para os testes automatizados,
    garantindo idempotência e independência entre as execuções.
    """
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        seed(session)
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    """
    Sobrescreve a dependência de sessão do FastAPI para usar o banco em memória.
    """
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture
def headers_admin() -> dict:
    token = criar_token(
        sub="admin",
        papel="admin",
        escopos=SCOPES_POR_PAPEL["admin"],
        mfa_verified=True,
    )
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def headers_admin_sem_mfa() -> dict:
    token = criar_token(
        sub="admin",
        papel="admin",
        escopos=SCOPES_POR_PAPEL["admin"],
        mfa_verified=False,  # Sem MFA verificado
    )
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def headers_medico1() -> dict:
    token = criar_token(
        sub="dr_carlos",
        papel="profissional_saude",
        escopos=SCOPES_POR_PAPEL["profissional_saude"],
        crm="123456-SP",
        mfa_verified=False,
    )
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def headers_medico2() -> dict:
    token = criar_token(
        sub="dra_ana",
        papel="profissional_saude",
        escopos=SCOPES_POR_PAPEL["profissional_saude"],
        crm="654321-RJ",
        mfa_verified=False,
    )
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def headers_recepcao() -> dict:
    token = criar_token(
        sub="recepcao",
        papel="recepcionista",
        escopos=SCOPES_POR_PAPEL["recepcionista"],
        mfa_verified=False,
    )
    return {"Authorization": f"Bearer {token}"}


@pytest.fixture
def headers_m2m_laboratorio() -> dict:
    token = criar_token(
        sub="m2m:laboratorio",
        papel="m2m_laboratorio",
        escopos=SCOPES_POR_PAPEL["m2m_laboratorio"],
        extra_claims={"client_id": "laboratorio-parceiro-01"},
    )
    return {"Authorization": f"Bearer {token}"}
