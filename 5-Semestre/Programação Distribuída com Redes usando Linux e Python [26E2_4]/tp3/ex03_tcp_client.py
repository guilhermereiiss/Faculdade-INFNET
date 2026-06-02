import socket
import threading
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9001
NUM_CLIENTES = 5


def cliente_tcp(cliente_id: int):
    mensagem = f"Cliente-{cliente_id}: " + ("X" * max(0, 10 - len(str(cliente_id)) - 10))
    mensagem = mensagem.ljust(10)   

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_HOST, SERVER_PORT))
            ip_local, porta_local = s.getsockname()
            print(f"[CLIENTE {cliente_id}] Conectado de {ip_local}:{porta_local}")

            s.sendall(mensagem.encode("utf-8"))
            resposta = s.recv(4096)
            print(f"[CLIENTE {cliente_id}] Echo recebido: {resposta.decode()!r}")
    except OSError as e:
        print(f"[CLIENTE {cliente_id}] Erro: {e}")


if __name__ == "__main__":
    threads = []
    for i in range(1, NUM_CLIENTES + 1):
        t = threading.Thread(target=cliente_tcp, args=(i,))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print(f"\n[INFO] {NUM_CLIENTES} clientes concluídos.")
