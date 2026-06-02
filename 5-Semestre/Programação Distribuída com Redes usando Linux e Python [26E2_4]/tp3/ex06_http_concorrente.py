
import socket
import multiprocessing
import os

HOST = "0.0.0.0"
PORT = 8081
BUFFER_SIZE = 4096

PAGINAS = {
    "/": b"<html><body><h1>RAIZ</h1></body></html>",
    "/health": b"<html><body><h1>HEALTH</h1></body></html>",
}
PAGINA_404 = b"<html><body><h1>NOT FOUND</h1></body></html>"


def construir_resposta(status_code: int, status_text: str, corpo: bytes) -> bytes:
    return (
        f"HTTP/1.1 {status_code} {status_text}\r\n"
        f"Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(corpo)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    ).encode() + corpo


def extrair_rota(raw: bytes) -> str:
    try:
        return raw.split(b"\r\n")[0].decode().split(" ")[1].split("?")[0]
    except Exception:
        return "/"


def handle_request(conn_fd: int, addr: tuple):
    """Executado em processo filho: recebe fd numérico para evitar herança de socket."""
    pid = os.getpid()
    ip, porta = addr
    with socket.fromfd(conn_fd, socket.AF_INET, socket.SOCK_STREAM) as conn:
        os.close(conn_fd)
        try:
            dados = conn.recv(BUFFER_SIZE)
            if not dados:
                return
            rota = extrair_rota(dados)
            print(f"[PID {pid}] {ip}:{porta} → {rota}")

            corpo = PAGINAS.get(rota, PAGINA_404)
            status = (200, "OK") if rota in PAGINAS else (404, "Not Found")
            conn.sendall(construir_resposta(*status, corpo))
        except OSError as e:
            print(f"[PID {pid}] ERRO: {e}")


def servidor_http_concorrente():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(20)
        print(f"[HTTP Concorrente] Escutando em http://{HOST}:{PORT}")
        print("  Teste: for i in $(seq 1 10); do curl -s http://localhost:8081/health & done; wait")
        print("-" * 60)

        processos: list[multiprocessing.Process] = []

        try:
            while True:
                conn, addr = s.accept()
                fd = conn.fileno()
                fd_dup = os.dup(fd)
                conn.close()

                p = multiprocessing.Process(
                    target=handle_request,
                    args=(fd_dup, addr),
                    daemon=True,
                )
                p.start()
                os.close(fd_dup)  

                processos.append(p)

                processos = [p for p in processos if p.is_alive()]

        except KeyboardInterrupt:
            print("\n[HTTP] Encerrando.")
        finally:
            for p in processos:
                p.join(timeout=2)

if __name__ == "__main__":
    servidor_http_concorrente()
