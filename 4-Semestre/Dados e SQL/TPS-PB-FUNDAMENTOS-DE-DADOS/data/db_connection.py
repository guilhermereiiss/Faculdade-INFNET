import psycopg2

def init_db():
    try:
        conn = psycopg2.connect(
            dbname="Loopify",
            user="postgres",
            password="gui123reis13",
            host="localhost",
            port="5433"
        )
        cursor = conn.cursor()

        # Tabela de clientes (já existente)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente_schema.cliente (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                senha VARCHAR(255) NOT NULL
            )
        ''')

        # Tabela de músicas (já existente)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS musicas_schema.musicas (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                genero TEXT NOT NULL,
                artista TEXT NOT NULL,
                data_criacao DATE NOT NULL
            )
        ''')

        # Tabela de playlists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS playlists_schema.playlists (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                cliente_id INTEGER NOT NULL,
                data_criacao DATE NOT NULL,
                FOREIGN KEY (cliente_id) REFERENCES cliente_schema.cliente(id) ON DELETE CASCADE
            )
        ''')

        # Tabela de relacionamento playlist_musicas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS playlists_schema.playlist_musicas (
                playlist_id INTEGER NOT NULL,
                musica_id INTEGER NOT NULL,
                FOREIGN KEY (playlist_id) REFERENCES playlists_schema.playlists(id) ON DELETE CASCADE,
                FOREIGN KEY (musica_id) REFERENCES musicas_schema.musicas(id) ON DELETE CASCADE,
                PRIMARY KEY (playlist_id, musica_id)
            )
        ''')

        conn.commit()
        cursor.close()
        conn.close()
        print("Banco de dados inicializado com sucesso!")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")

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