from data.db_connection import get_db_connection
import datetime

def criar_playlist(nome, cliente_id):
    try:
        conn = get_db_connection()
        if conn is None:
            print("Falha na conexão com o banco de dados.")
            return
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO playlists_schema.playlists (nome, cliente_id, data_criacao)
            VALUES (%s, %s, %s)
        ''', (nome, cliente_id, datetime.date.today()))

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Playlist '{nome}' criada com sucesso!")
    except Exception as e:
        print(f"Erro ao criar playlist: {e}")

def listar_playlists(cliente_id):
    try:
        conn = get_db_connection()
        if conn is None:
            print("Falha na conexão com o banco de dados.")
            return
        cursor = conn.cursor()

        cursor.execute('''
            SELECT id, nome
            FROM playlists_schema.playlists
            WHERE cliente_id = %s
        ''', (cliente_id,))
        playlists = cursor.fetchall()

        if not playlists:
            print("Nenhuma playlist encontrada!")
            return

        print("\n--- Suas Playlists ---")
        for playlist in playlists:
            id_playlist, nome = playlist
            print(f"[{id_playlist}] {nome}")
        print("----------------------")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao listar playlists: {e}")

def adicionar_musica_playlist(playlist_id, musica_id):
    try:
        conn = get_db_connection()
        if conn is None:
            print("Falha na conexão com o banco de dados.")
            return
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO playlists_schema.playlist_musicas (playlist_id, musica_id)
            VALUES (%s, %s)
            RETURNING (SELECT nome FROM musicas_schema.musicas WHERE id = %s)
        ''', (playlist_id, musica_id, musica_id))
        result = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        if result:
            print(f"Música '{result[0]}' adicionada à playlist!")
        else:
            print("Música ou playlist não encontrada!")
    except Exception as e:
        print(f"Erro ao adicionar música à playlist: {e}")

def remover_playlist(playlist_id, cliente_id):
    try:
        conn = get_db_connection()
        if conn is None:
            print("Falha na conexão com o banco de dados.")
            return
        cursor = conn.cursor()

        cursor.execute('''
            DELETE FROM playlists_schema.playlists
            WHERE id = %s AND cliente_id = %s
            RETURNING nome
        ''', (playlist_id, cliente_id))
        result = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        if result:
            print(f"Playlist '{result[0]}' removida com sucesso!")
        else:
            print("Playlist não encontrada ou você não tem permissão para removê-la!")
    except Exception as e:
        print(f"Erro ao remover playlist: {e}")

def listar_musicas_playlist(playlist_id, cliente_id):
    try:
        conn = get_db_connection()
        if conn is None:
            print("Falha na conexão com o banco de dados.")
            return
        cursor = conn.cursor()

        cursor.execute('''
            SELECT m.id, m.nome, m.artista, m.genero
            FROM musicas_schema.musicas m
            JOIN playlists_schema.playlist_musicas pm ON m.id = pm.musica_id
            JOIN playlists_schema.playlists p ON pm.playlist_id = p.id
            WHERE pm.playlist_id = %s AND p.cliente_id = %s
        ''', (playlist_id, cliente_id))
        musicas = cursor.fetchall()

        if not musicas:
            print("Nenhuma música encontrada na playlist!")
            return

        print("\n--- Músicas na Playlist ---")
        for musica in musicas:
            id_musica, nome, artista, genero = musica
            print(f"[{id_musica}] {nome} - {artista} ({genero})")
        print("--------------------------")

        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao listar músicas da playlist: {e}")

def listar_musicas_disponiveis():
    try:
        conn = get_db_connection()
        if conn is None:
            print("Falha na conexão com o banco de dados.")
            return
        
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, nome, artista, genero 
            FROM musicas_schema.musicas 
            ORDER BY nome
        ''')
        musicas = cursor.fetchall()
        
        if not musicas:
            print("Nenhuma música cadastrada no sistema.")
        else:
            print("\n=== Músicas Disponíveis ===")
            for m in musicas:
                print(f"[{m[0]}] {m[1]} - {m[2]} ({m[3]})")
            print("==========================\n")
        
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erro ao listar músicas: {e}")

