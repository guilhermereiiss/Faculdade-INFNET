
import socket
import sys
import time

HOST_IPV6 = "::1"
PORT = 9006
BUFFER_SIZE = 4096


def servidor_ipv6():
    print("[IPv6 SERVIDOR] Iniciando em tcp://[::1]:{}".format(PORT))
    try:
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
            # IPV6_V6ONLY=1 garante que o socket escute somente IPv6
            s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 1)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((HOST_IPV6, PORT))
            s.listen(5)
            print(f"[IPv6 SERVIDOR] Aguardando conexões em {s.getsockname()}")
            print("-" * 50)

            conn, addr = s.accept()
            with conn:
                ip, porta, *_ = addr
                print(f"[IPv6 SERVIDOR] Conexão recebida de [{ip}]:{porta}")
                while True:
                    dados = conn.recv(BUFFER_SIZE)
                    if not dados:
                        break
                    mensagem = dados.decode("utf-8", errors="replace")
                    print(f"[IPv6 SERVIDOR] Recebido: {mensagem!r}")
                    conn.sendall(dados)   # echo
                print("[IPv6 SERVIDOR] Cliente desconectou.")

    except OSError as e:
        print(f"[IPv6 SERVIDOR] ERRO: {e}")
        print("  → Verifique se IPv6 está habilitado no sistema.")
        print("  → Linux: cat /proc/net/if_inet6  |  ip -6 addr show lo")
        print("  → Windows: ipconfig | findstr /i '::1'")
        raise SystemExit(1)


def cliente_ipv6():
    print(f"[IPv6 CLIENTE] Conectando a [{HOST_IPV6}]:{PORT}")
    try:
        with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
            s.connect((HOST_IPV6, PORT, 0, 0))
            ip_local, porta_local, *_ = s.getsockname()
            print(f"[IPv6 CLIENTE] Conectado. Local: [{ip_local}]:{porta_local}")

            for i in range(1, 4):
                mensagem = f"Mensagem IPv6 #{i} via ::1"
                s.sendall(mensagem.encode("utf-8"))
                time.sleep(0.1)
                resposta = s.recv(BUFFER_SIZE)
                print(f"[IPv6 CLIENTE] Echo: {resposta.decode()!r}")

    except OSError as e:
        print(f"[IPv6 CLIENTE] ERRO: {e}")
        print("  → Servidor pode não estar rodando ou IPv6 está desabilitado.")
        raise SystemExit(1)

if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "servidor"
    if modo == "cliente":
        cliente_ipv6()
    else:
        servidor_ipv6()
