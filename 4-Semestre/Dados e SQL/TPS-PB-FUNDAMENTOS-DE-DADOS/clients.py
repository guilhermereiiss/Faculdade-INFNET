import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname="Loopify",
            user="postgres",
            password="gui123reis13",
            host="localhost",
            port="5433"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def list_clients():
    try:
        conn = get_db_connection()
        if conn is None:
            print("Falha na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()
        cursor.execute('SELECT nome, email FROM cliente_schema.cliente')
        clients = cursor.fetchall()
        
        if not clients:
            print("Nenhum cliente encontrado.")
        else:
            print("\n=== Lista de Clientes ===")
            for client in clients:
                nome, email = client
                print(f"Nome: {nome} | Email: {email}")
            print("========================")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao listar clientes: {e}")

if __name__ == "__main__":
    list_clients()