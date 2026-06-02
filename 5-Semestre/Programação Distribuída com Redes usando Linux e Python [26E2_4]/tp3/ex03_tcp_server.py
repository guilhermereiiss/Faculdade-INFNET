import socket
import multiprocessing

HOST = "0.0.0.0"
PORT = 9001
BUFFER_SIZE = 4096


def handle_client(conn: socket.socket, addr: tuple):
    """Trata um cliente individualmente (executado em processo filho)."""
    ip, porta = addr
    print(f"[PROCESSO {multiprocessing.current_process().pid}] "
          f"Conexão recebida de {ip}:{porta}")

    try:
        while True:
            dados = conn.recv(BUFFER_SIZE)
            if not dados:
                break
            mensagem = dados.decode("utf-8", errors="replace")
            print(f"  [MSG de {ip}:{porta}] {mensagem}")
            conn.sendall(dados)  
    except OSError as e:
        print(f"  [ERRO no cliente {ip}:{porta}] {e}")
    finally:
        conn.close()
        print(f"[PROCESSO {multiprocessing.current_process().pid}] "
              f"Conexão encerrada: {ip}:{porta}")


def servidor_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(10)
        print(f"[SERVIDOR] Aguardando conexões TCP em {HOST}:{PORT}")
        print("-" * 50)

        processos: list[multiprocessing.Process] = []

        try:
            while True:
                conn, addr = s.accept()
                p = multiprocessing.Process(
                    target=handle_client,
                    args=(conn, addr),
                    daemon=True,
                )
                p.start()
                processos.append(p)
                conn.close()   
        except KeyboardInterrupt:
            print("\n[SERVIDOR] Encerrando.")
        finally:
            for p in processos:
                p.join(timeout=1)

if __name__ == "__main__":
    servidor_tcp()
