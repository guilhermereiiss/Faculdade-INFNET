
import socket
import os
import sys

HOST   = "127.0.0.1"
PORT   = 9007
BUFFER = 4096


def servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        print(f"[SERVIDOR] Aguardando arquivo em {HOST}:{PORT}")

        conn, addr = s.accept()
        with conn:
            print(f"[SERVIDOR] Conexão de {addr[0]}:{addr[1]}")

            nome_bytes = b""
            while b"\n" not in nome_bytes:
                chunk = conn.recv(1)
                if not chunk:
                    raise ConnectionError("Conexão encerrada ao receber nome.")
                nome_bytes += chunk
            nome_recebido = nome_bytes.strip().decode("utf-8")

            tamanho_bytes = b""
            while b"\n" not in tamanho_bytes:
                chunk = conn.recv(1)
                if not chunk:
                    raise ConnectionError("Conexão encerrada ao receber tamanho.")
                tamanho_bytes += chunk
            tamanho_esperado = int(tamanho_bytes.strip())

            conteudo = b""
            while len(conteudo) < tamanho_esperado:
                falta = tamanho_esperado - len(conteudo)
                chunk = conn.recv(min(BUFFER, falta))
                if not chunk:
                    break
                conteudo += chunk

            nome_salvo = "recebido_" + nome_recebido
            with open(nome_salvo, "wb") as f:
                f.write(conteudo)

            print(f"\n[SERVIDOR] Nome recebido  : {nome_recebido}")
            print(f"[SERVIDOR] Tamanho recebido: {len(conteudo)} bytes (esperado: {tamanho_esperado})")
            print(f"[SERVIDOR] Conteúdo (início): {conteudo[:200]}")
            print(f"[SERVIDOR] Salvo como       : {nome_salvo}")


def cliente(caminho_arquivo: str):
    if not os.path.exists(caminho_arquivo):
        caminho_arquivo = "exemplo.txt"
        with open(caminho_arquivo, "w") as f:
            f.write("Conteúdo de exemplo para transferência via TCP.\n" * 20)
        print(f"[CLIENTE] Arquivo '{caminho_arquivo}' criado como exemplo.")

    nome_arquivo = os.path.basename(caminho_arquivo)
    with open(caminho_arquivo, "rb") as f:
        conteudo = f.read()
    tamanho = len(conteudo)

    print(f"\n[CLIENTE] Nome   : {nome_arquivo}")
    print(f"[CLIENTE] Tamanho: {tamanho} bytes")
    print(f"[CLIENTE] Conteúdo (início): {conteudo[:200]}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"\n[CLIENTE] Conectado a {HOST}:{PORT}")

        s.send((nome_arquivo + "\n").encode("utf-8"))
        print("[CLIENTE] Nome enviado.")

        s.send((str(tamanho) + "\n").encode("utf-8"))
        print("[CLIENTE] Tamanho enviado.")

        s.send(conteudo)
        print("[CLIENTE] Conteúdo enviado.")


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "servidor"
    if modo == "cliente":
        arquivo = sys.argv[2] if len(sys.argv) > 2 else "exemplo.txt"
        cliente(arquivo)
    else:
        servidor()
