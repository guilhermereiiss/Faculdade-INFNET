
import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(certfile='server.crt', keyfile='server.key')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(5)

print(f"[Servidor] esperando conexao em {HOST}:{PORT}")

tls_sock = ctx.wrap_socket(sock, server_side=True)

while True:
    conn, addr = tls_sock.accept()
    print(f"[Servidor] conectou: {addr}")
    dados = conn.recv(4096)
    msg = dados.decode('utf-8', errors='replace')
    print(f"[Servidor] Comando Seguro Recebido: {msg}")
    conn.close()
