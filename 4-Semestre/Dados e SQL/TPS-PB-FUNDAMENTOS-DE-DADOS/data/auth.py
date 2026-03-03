import psycopg2
from data.db_connection import get_db_connection

def verificar_login(email, password):
    try:
        conn = get_db_connection()
        if conn is None:
            return False, None, None
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT id, nome FROM cliente_schema.cliente
            WHERE email = %s AND senha = %s
        ''', (email, password))
        
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if usuario:
            cliente_id, nome = usuario
            print(f"Bem-vindo, {nome}!")
            return True, nome, cliente_id
        else:
            print("Email ou senha inválidos!")
            return False, None, None
    except Exception as e:
        print(f"Erro ao verificar login: {e}")
        return False, None, None