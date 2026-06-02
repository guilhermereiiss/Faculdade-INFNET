import socket

configs = [
    (socket.AF_INET,  socket.SOCK_STREAM, "AF_INET  + SOCK_STREAM (IPv4/TCP)"),
    (socket.AF_INET,  socket.SOCK_DGRAM,  "AF_INET  + SOCK_DGRAM  (IPv4/UDP)"),
    (socket.AF_INET6, socket.SOCK_STREAM, "AF_INET6 + SOCK_STREAM (IPv6/TCP)"),
    (socket.AF_INET6, socket.SOCK_DGRAM,  "AF_INET6 + SOCK_DGRAM  (IPv6/UDP)"),
]

HOST_IPV4 = "127.0.0.1"
HOST_IPV6 = "::1"
PORT = 12345

print("=" * 60)
print("INVENTÁRIO DE SOCKETS")
print("=" * 60)

for family, sock_type, descricao in configs:
    host = HOST_IPV6 if family == socket.AF_INET6 else HOST_IPV4
    s = None
    try:
        s = socket.socket(family, sock_type)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, PORT))

        if sock_type == socket.SOCK_STREAM:
            s.listen(1)

        print(f"[OK]    {descricao}")
        print(f"        Endereço local: {s.getsockname()}")

    except OSError as e:
        print(f"[ERRO]  {descricao}")
        print(f"        Erro: {e}")

    finally:
        if s:
            s.close()

print("=" * 60)
print("""
JUSTIFICATIVA TÉCNICA:
- AF_INET + SOCK_STREAM  → IPv4/TCP: sempre disponível; bind em 127.0.0.1 funciona.
- AF_INET + SOCK_DGRAM   → IPv4/UDP: sempre disponível; bind em 127.0.0.1 funciona.
- AF_INET6 + SOCK_STREAM → IPv6/TCP: depende do SO ter IPv6 habilitado e suporte
  à interface loopback ::1. Falha se o kernel não tiver módulo IPv6 carregado.
- AF_INET6 + SOCK_DGRAM  → IPv6/UDP: mesma dependência do item acima. Em ambientes
  com IPv6 desabilitado (ex.: containers mínimos), o bind em ::1 retorna EADDRNOTAVAIL.
""")
