from typing import Optional, List, Generator
from sqlmodel import SQLModel, create_engine, Session, select
from config import settings
from models.usuario import Usuario
from models.paciente import Paciente
from models.profissional import Profissional
from models.consulta import Consulta
from auth.security import hash_password

# Configuração do SQLite com suporte a multithreading no FastAPI
connect_args = {"check_same_thread": False} if "sqlite" in settings.database_url else {}
engine = create_engine(settings.database_url, echo=False, connect_args=connect_args)


def get_session() -> Generator[Session, None, None]:
    """
    Injeção de dependência FastAPI para sessões do banco de dados (Exercício 11).
    Garante fechamento seguro da sessão após o término da requisição.
    """
    with Session(engine) as session:
        yield session


def criar_tabelas() -> None:
    """Cria o esquema relacional se ainda não existir."""
    SQLModel.metadata.create_all(engine)


def obter_usuario_por_username(session: Session, username: str) -> Optional[Usuario]:
    """Query parametrizada — previne SQL Injection (Exercício 11)."""
    statement = select(Usuario).where(Usuario.username == username)
    return session.exec(statement).first()


def obter_consulta_por_id(session: Session, consulta_id: int) -> Optional[Consulta]:
    """Query parametrizada — previne SQL Injection (Exercício 11)."""
    statement = select(Consulta).where(Consulta.id == consulta_id)
    return session.exec(statement).first()


def obter_paciente_por_id(session: Session, paciente_id: int) -> Optional[Paciente]:
    """Query parametrizada."""
    statement = select(Paciente).where(Paciente.id == paciente_id)
    return session.exec(statement).first()


def obter_paciente_por_cpf(session: Session, cpf: str) -> Optional[Paciente]:
    """Query parametrizada."""
    statement = select(Paciente).where(Paciente.cpf == cpf)
    return session.exec(statement).first()


def obter_profissional_por_id(session: Session, profissional_id: int) -> Optional[Profissional]:
    """Query parametrizada."""
    statement = select(Profissional).where(Profissional.id == profissional_id)
    return session.exec(statement).first()


def obter_profissional_por_crm(session: Session, crm: str) -> Optional[Profissional]:
    """Query parametrizada."""
    statement = select(Profissional).where(Profissional.crm == crm)
    return session.exec(statement).first()


def obter_profissional_por_username(session: Session, username: str) -> Optional[Profissional]:
    """Query parametrizada."""
    statement = select(Profissional).where(Profissional.username == username)
    return session.exec(statement).first()


def seed(session: Session) -> None:
    """
    Popula o banco inicial com dados de teste para os três papéis de usuário
    e entidades do domínio médico.
    """
    # 1. Usuários
    if not session.exec(select(Usuario)).first():
        usuarios = [
            Usuario(
                username="admin",
                email="admin@clinica.com.br",
                hashed_password=hash_password("Admin@123456"),
                papel="admin",
                mfa_enabled=True,
                mfa_secret=settings.admin_mfa_secret,
            ),
            Usuario(
                username="dr_carlos",
                email="carlos@clinica.com.br",
                hashed_password=hash_password("Medico@123456"),
                papel="profissional_saude",
                crm="123456-SP",
                mfa_enabled=False,
            ),
            Usuario(
                username="dra_ana",
                email="ana@clinica.com.br",
                hashed_password=hash_password("Medico@123456"),
                papel="profissional_saude",
                crm="654321-RJ",
                mfa_enabled=False,
            ),
            Usuario(
                username="recepcao",
                email="recepcao@clinica.com.br",
                hashed_password=hash_password("Recepcao@123456"),
                papel="recepcionista",
                mfa_enabled=False,
            ),
        ]
        session.add_all(usuarios)
        session.commit()

    # 2. Profissionais
    if not session.exec(select(Profissional)).first():
        profissionais = [
            Profissional(
                nome="Dr. Carlos Silva",
                crm="123456-SP",
                especialidade="Cardiologia",
                username="dr_carlos",
                email="carlos@clinica.com.br",
            ),
            Profissional(
                nome="Dra. Ana Santos",
                crm="654321-RJ",
                especialidade="Dermatologia",
                username="dra_ana",
                email="ana@clinica.com.br",
            ),
        ]
        session.add_all(profissionais)
        session.commit()

    # 3. Pacientes (com dados protegidos pela LGPD)
    if not session.exec(select(Paciente)).first():
        pacientes = [
            Paciente(
                nome="João Pereira da Silva",
                cpf="11122233344",
                data_nascimento="1985-04-12",
                telefone="11988887777",
                email="joao.silva@email.com",
                endereco="Av. Paulista, 1000 - São Paulo, SP",
                historico_alergias="Alergia severa a Penicilina e Dipirona",
                auditoria_criado_por="recepcao",
            ),
            Paciente(
                nome="Maria Eduarda Oliveira",
                cpf="55566677788",
                data_nascimento="1992-09-25",
                telefone="21977776666",
                email="maria.oliveira@email.com",
                endereco="Rua das Flores, 45 - Rio de Janeiro, RJ",
                historico_alergias="Sem alergias medicamentosas conhecidas",
                auditoria_criado_por="recepcao",
            ),
        ]
        session.add_all(pacientes)
        session.commit()

    # 4. Consultas Iniciais
    if not session.exec(select(Consulta)).first():
        consultas = [
            Consulta(
                paciente_id=1,
                profissional_id=1,
                data_hora="2026-09-20T09:00:00",
                status="agendada",
                motivo="Avaliação de arritmia cardíaca",
                prontuario_diagnostico="Paciente relata palpitações aos esforços. ECG solicitado.",
                observacoes="Paciente deve trazer exames anteriores.",
                auditoria_criado_por="dr_carlos",
            ),
            Consulta(
                paciente_id=2,
                profissional_id=2,
                data_hora="2026-09-20T10:30:00",
                status="agendada",
                motivo="Consulta de rotina dermatológica",
                prontuario_diagnostico="Inspeção cutânea sem lesões atípicas.",
                observacoes="Retorno em 6 meses.",
                auditoria_criado_por="dra_ana",
            ),
        ]
        session.add_all(consultas)
        session.commit()
