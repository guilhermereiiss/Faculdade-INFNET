import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.dialects.postgresql import insert

# CONFIGURAÇÕES DO BANCO
DATABASE_URL = "postgresql://postgres:gui123reis13@localhost:5433/tp3-pb"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# MODELO ORM
class Cliente(Base):
    __tablename__ = "clientes"
    __table_args__ = {"schema": "mercadinho"}

    id_cliente = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)
    cpf = Column(String(14))
    telefone = Column(String(20))
    endereco = Column(String(255))


# UPSERT
def upsert_clientes(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    for cliente in data["clientes"]:
        stmt = insert(Cliente).values(cliente)

        upsert_stmt = stmt.on_conflict_do_update(
            index_elements=["id_cliente"],  
            set_={
                "nome": stmt.excluded.nome,
                "cpf": stmt.excluded.cpf,
                "telefone": stmt.excluded.telefone,
                "endereco": stmt.excluded.endereco
            }
        )

        session.execute(upsert_stmt)

    session.commit()
    print("UPSERT concluído com sucesso!")


if __name__ == "__main__":
    upsert_clientes(r"C:\Users\gabib\OneDrive\Documentos\TPS DE PB\TP4\clientes_upsert.json")

