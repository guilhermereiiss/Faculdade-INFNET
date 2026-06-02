
import ssl
import socket
import os

HOST = "0.0.0.0"
PORT = 8443
CERT_FILE = "server.crt"
KEY_FILE  = "server.key"

RESPOSTA_HTTP = (
    b"HTTP/1.1 200 OK\r\n"
    b"Content-Type: text/plain; charset=utf-8\r\n"
    b"Content-Length: 26\r\n"
    b"Connection: close\r\n"
    b"\r\n"
    b"Resposta via TLS local\r\n\r\n"
)


def verificar_certificados():
    if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
        print("[ERRO] Certificado ou chave não encontrados.")
        print("Execute:")
        print('  openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt \\')
        print('    -days 365 -nodes -subj "/CN=localhost"')
        raise SystemExit(1)


def servidor_tls():
    verificar_certificados()

    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as raw_sock:
        raw_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        raw_sock.bind((HOST, PORT))
        raw_sock.listen(5)
        print(f"[TLS] Servidor escutando em https://{HOST}:{PORT}")
        print("  Teste: curl -k https://localhost:8443/")
        print("-" * 50)

        with ctx.wrap_socket(raw_sock, server_side=True) as tls_sock:
            try:
                while True:
                    conn, addr = tls_sock.accept()
                    ip, porta = addr
                    print(f"[TLS] Conexão de {ip}:{porta} | "
                          f"cipher={conn.cipher()[0]} | versão={conn.version()}")
                    try:
                        conn.recv(4096) 
                        conn.sendall(RESPOSTA_HTTP)
                    except ssl.SSLError as e:
                        print(f"  [SSL ERRO] {e}")
                    finally:
                        conn.close()
            except KeyboardInterrupt:
                print("\n[TLS] Encerrando.")


if __name__ == "__main__":
    servidor_tls()
