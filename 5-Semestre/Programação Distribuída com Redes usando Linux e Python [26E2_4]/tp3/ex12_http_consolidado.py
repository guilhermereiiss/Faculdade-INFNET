

import socket
import datetime

HOST = "0.0.0.0"
PORT = 8082
BUFFER_SIZE = 4096

ROTAS = {
    "/": (200, "OK",        b"OK"),
    "/admin": (403, "Forbidden", b"Forbidden"),
}



def construir_resposta(status: int, status_text: str, corpo: bytes) -> bytes:
    return (
        f"HTTP/1.1 {status} {status_text}\r\n"
        f"Content-Type: text/plain; charset=utf-8\r\n"
        f"Content-Length: {len(corpo)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    ).encode() + corpo


def extrair_metadados(raw: bytes) -> tuple[str, str, str]:
    """Retorna (método, rota, versão_http)."""
    try:
        primeira = raw.split(b"\r\n")[0].decode("utf-8", errors="replace")
        partes = primeira.split(" ")
        metodo  = partes[0] if len(partes) > 0 else "?"
        rota    = partes[1].split("?")[0] if len(partes) > 1 else "/"
        versao  = partes[2] if len(partes) > 2 else "HTTP/?"
        return metodo, rota, versao
    except Exception:
        return "?", "/", "HTTP/?"


def tratar_conexao(conn: socket.socket, addr: tuple):
    ip, porta = addr
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        raw = conn.recv(BUFFER_SIZE)
        if not raw:
            return

        metodo, rota, versao = extrair_metadados(raw)
        print(f"[{agora}] {ip}:{porta} → {metodo} {rota} {versao}")

        if rota in ROTAS:
            status, status_text, corpo = ROTAS[rota]
        else:
            status, status_text, corpo = 404, "Not Found", b"Not Found"

        resposta = construir_resposta(status, status_text, corpo)
        conn.sendall(resposta)
        print(f"           ← {status} {status_text}")

    except OSError as e:
        print(f"[ERRO] {e}")
    finally:
        conn.close()


def servidor_http():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(10)
        print(f"[HTTP] Serviço consolidado em http://{HOST}:{PORT}")
        print("  / → 200   /admin → 403   <outros> → 404")
        print("  Teste:")
        print("    curl -v http://localhost:8082/")
        print("    curl -v http://localhost:8082/admin")
        print("    curl -v http://localhost:8082/pagina-inexistente")
        print("-" * 55)

        try:
            while True:
                conn, addr = s.accept()
                tratar_conexao(conn, addr)
        except KeyboardInterrupt:
            print("\n[HTTP] Encerrando.")


if __name__ == "__main__":
    servidor_http()
