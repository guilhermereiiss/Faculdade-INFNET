import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from upsert_clientes import Cliente


DATABASE_URL = "postgresql://postgres:gui123reis13@localhost:5433/tp3-pb"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()


def delete_clientes(json_path):
    with open(json_path, "r") as f:
        data = json.load(f)

    ids = data["delete_ids"]

    for cid in ids:
        try:
            session.query(Cliente).filter(Cliente.id_cliente == cid).delete()
            session.commit()
            print(f"Cliente {cid} deletado.")
        except Exception as e:
            session.rollback()
            print(f"Cliente {cid} NÃO pode ser deletado. Motivo: {e}")



if __name__ == "__main__":
    delete_clientes("C:/Users/gabib/OneDrive/Documentos/TPS DE PB/TP4/clientes_delete.json")


