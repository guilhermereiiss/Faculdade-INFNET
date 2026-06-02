import socket

HOST = "0.0.0.0"
PORT = 8080
BUFFER_SIZE = 4096

PAGINAS = {
    "/": b"<html><body><h1>RAIZ</h1></body></html>",
    "/health": b"<html><body><h1>HEALTH</h1></body></html>",
}

PAGINA_404 = b"<html><body><h1>NOT FOUND</h1></body></html>"


def construir_resposta(status_code: int, status_text: str, corpo: bytes) -> bytes:
    status_line  = f"HTTP/1.1 {status_code} {status_text}\r\n".encode()
    headers  = (
        f"Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(corpo)}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    ).encode()
    return status_line + headers + corpo


def extrair_rota(request_raw: bytes) -> str:
    try:
        primeira_linha = request_raw.split(b"\r\n")[0].decode()
        partes = primeira_linha.split(" ")
        if len(partes) >= 2:
            return partes[1].split("?")[0]   
    except Exception:
        pass
    return "/"


def tratar_conexao(conn: socket.socket, addr: tuple):
    ip, porta = addr
    try:
        dados = conn.recv(BUFFER_SIZE)
        if not dados:
            return

        rota = extrair_rota(dados)
        print(f"[{ip}:{porta}] {dados.split(b'\\r\\n')[0].decode(errors='replace')}")

        if rota in PAGINAS:
            resposta = construir_resposta(200, "OK", PAGINAS[rota])
        else:
            resposta = construir_resposta(404, "Not Found", PAGINA_404)

        conn.sendall(resposta)
    except OSError as e:
        print(f"[ERRO] {e}")
    finally:
        conn.close()


def servidor_http():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(5)
        print(f"[HTTP] Servidor escutando em http://{HOST}:{PORT}")
        print("  Rotas: /  e  /health")
        print("  Teste: curl -v http://localhost:8080/")
        print("-" * 50)

        try:
            while True:
                conn, addr = s.accept()
                tratar_conexao(conn, addr)
        except KeyboardInterrupt:
            print("\n[HTTP] Encerrando.")

if __name__ == "__main__":
    servidor_http()
