from funcoes import (
    criar_playlist, listar_playlists, adicionar_musica_playlist, 
    remover_playlist, listar_musicas_playlist, listar_musicas_disponiveis
)
from data.db_connection import init_db
from data.auth import verificar_login
import datetime  

def login():
    print("\n=== Login Loopify ===")
    email = input("Email: ")
    password = input("Senha: ")
    return verificar_login(email, password)

def menu(cliente_id):
    while True:
        print("\n=== Loopify - Gerenciador de Playlists ===")
        print("1 - Criar playlist")
        print("2 - Listar playlists")
        print("3 - Adicionar música a playlist")
        print("4 - Remover playlist")
        print("5 - Listar músicas de uma playlist")
        print("6 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome da playlist: ")
            criar_playlist(nome, cliente_id)

        elif opcao == "2":
            listar_playlists(cliente_id)

        elif opcao == "3":
            listar_playlists(cliente_id)
            try:
                playlist_id = int(input("ID da playlist: "))
            except ValueError:
                print("ID inválido! Use apenas números.")
                continue

            listar_musicas_disponiveis()

            try:
                musica_id = int(input("ID da música para adicionar: "))
                adicionar_musica_playlist(playlist_id, musica_id)
            except ValueError:
                print("ID inválido! Use apenas números.")

        elif opcao == "4":
            listar_playlists(cliente_id)
            try:
                playlist_id = int(input("ID da playlist a remover: "))
                remover_playlist(playlist_id, cliente_id)
            except ValueError:
                print("ID inválido! Use apenas números.")

        elif opcao == "5":
            listar_playlists(cliente_id)
            try:
                playlist_id = int(input("ID da playlist: "))
                listar_musicas_playlist(playlist_id, cliente_id)
            except ValueError:
                print("ID inválido! Use apenas números.")

        elif opcao == "6":
            print("Saindo do Loopify...")
            break

        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    init_db()  # Inicializa o banco de dados primeiro
    success, nome, cliente_id = login()  # Chama login()
    if success and cliente_id is not None:
        print(f"Login realizado com sucesso para {nome} (ID: {cliente_id})")
        menu(cliente_id)
    else:
        print("Acesso negado. Encerrando o programa.")