# cliente.py
# rodar depois que o servidor.py ja estiver no ar

import socket
import ssl

HOST = '127.0.0.1'
PORT = 8443

msg = "AUTH_TOKEN:XYZ123:CMD:REBOOT_SERVER"

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.load_verify_locations('server.crt')
ctx.check_hostname = True
ctx.verify_mode = ssl.CERT_REQUIRED

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tls_sock = ctx.wrap_socket(sock, server_hostname=HOST)
tls_sock.connect((HOST, PORT))

print(f"[Cliente] conectado via TLS ({tls_sock.version()})")
tls_sock.sendall(msg.encode('utf-8'))
print(f"[Cliente] mandei: {msg}")

tls_sock.close()
