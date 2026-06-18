import socket

HOST = "127.0.0.1"
PORT = 5050
TAMANHO_CABECALHO = 4  


def recv_exato(conexao, n):
    dados = b""
    while len(dados) < n:
        pedaco = conexao.recv(n - len(dados))
        if not pedaco:
            break
        dados += pedaco
    return dados


def tratar_cliente(conexao, endereco):
    print(f"[SERVIDOR] Conexao aberta: {endereco}")
    try:
        while True:
            cabecalho = recv_exato(conexao, TAMANHO_CABECALHO)
            if len(cabecalho) < TAMANHO_CABECALHO:
                print(f"[SERVIDOR] Conexao encerrada por {endereco}")
                break

            tamanho_declarado = int.from_bytes(cabecalho, byteorder="big")

            conteudo = recv_exato(conexao, tamanho_declarado)
            tamanho_recebido = len(conteudo)

            if tamanho_recebido != tamanho_declarado:
                print(
                    f"[SERVIDOR] INCONSISTENCIA: declarado={tamanho_declarado} "
                    f"recebido={tamanho_recebido}"
                )
                resposta = f"ERRO: tamanho inconsistente (declarado={tamanho_declarado}, recebido={tamanho_recebido})"
                resposta_bytes = resposta.encode("utf-8")
                conexao.sendall(len(resposta_bytes).to_bytes(TAMANHO_CABECALHO, "big") + resposta_bytes)
                break  # conexao corrompida, nao ha como continuar com confianca

            texto = conteudo.decode("utf-8", errors="replace")
            print(f"[SERVIDOR] Mensagem recebida de {endereco}: {texto!r} ({tamanho_recebido} bytes)")

            resposta = f"OK: recebido {tamanho_recebido} bytes"
            resposta_bytes = resposta.encode("utf-8")
            conexao.sendall(len(resposta_bytes).to_bytes(TAMANHO_CABECALHO, "big") + resposta_bytes)

    except ConnectionResetError:
        print(f"[SERVIDOR] Conexao resetada por {endereco}")
    finally:
        conexao.close()
        print(f"[SERVIDOR] Conexao fechada: {endereco}")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen(5)
        print(f"[SERVIDOR] Escutando em {HOST}:{PORT}")

        while True:
            conexao, endereco = servidor.accept()
            tratar_cliente(conexao, endereco)


if __name__ == "__main__":
    main()