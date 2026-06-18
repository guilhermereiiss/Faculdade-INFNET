
import socket

HOST = "127.0.0.1"
PORT = 5050
TAMANHO_CABECALHO = 4  


def enviar_mensagem(conexao, texto):
    dados = texto.encode("utf-8")
    cabecalho = len(dados).to_bytes(TAMANHO_CABECALHO, byteorder="big")
    conexao.sendall(cabecalho + dados)


def recv_exato(conexao, n):
    dados = b""
    while len(dados) < n:
        pedaco = conexao.recv(n - len(dados))
        if not pedaco:
            break
        dados += pedaco
    return dados


def receber_resposta(conexao):
    cabecalho = recv_exato(conexao, TAMANHO_CABECALHO)
    if len(cabecalho) < TAMANHO_CABECALHO:
        return None
    tamanho = int.from_bytes(cabecalho, byteorder="big")
    conteudo = recv_exato(conexao, tamanho)
    return conteudo.decode("utf-8", errors="replace")


def main():
    mensagens = [
        "Primeira mensagem do cliente",
        "Segunda mensagem, um pouco mais longa que a primeira",
        "Terceira e ultima mensagem desta conexao",
    ]

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
        cliente.connect((HOST, PORT))
        print(f"[CLIENTE] Conectado a {HOST}:{PORT}")

        for msg in mensagens:
            print(f"[CLIENTE] Enviando: {msg!r}")
            enviar_mensagem(cliente, msg)

            resposta = receber_resposta(cliente)
            print(f"[CLIENTE] Resposta do servidor: {resposta!r}")

        print("[CLIENTE] Todas as mensagens foram enviadas. Encerrando conexao.")


if __name__ == "__main__":
    main()