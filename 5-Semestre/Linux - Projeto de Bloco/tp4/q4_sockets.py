
import socket
import sys
import time
import threading

TCP_PORT = 65432
UDP_PORT = 65433


def tcp_server(host="0.0.0.0", port=TCP_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        print(f"[TCP] Servidor em {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(b"ECHO: " + data)


def tcp_client(host="127.0.0.1", port=TCP_PORT):
    msgs = ["Olá servidor!", "Testando TCP", "Mensagem 3", "Dados 4", "Última"]
    results = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        for msg in msgs:
            t0 = time.perf_counter()
            s.sendall((msg + "\n").encode())
            resp = s.recv(1024).decode().strip()
            rtt = (time.perf_counter() - t0) * 1000
            results.append((msg, resp, rtt))
            print(f"  [{rtt:.3f}ms] {msg!r} -> {resp!r}")
    avg = sum(r[2] for r in results) / len(results)
    print(f"\n  RTT médio TCP: {avg:.3f} ms | {len(results)} mensagens")


def udp_server(host="0.0.0.0", port=UDP_PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"[UDP] Servidor em {host}:{port}")
        while True:
            data, addr = s.recvfrom(1024)
            s.sendto(b"ECHO: " + data, addr)


def udp_client(host="127.0.0.1", port=UDP_PORT):
    msgs = [f"Pacote UDP {i}" for i in range(1, 6)]
    results = []
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(2.0)
        for msg in msgs:
            t0 = time.perf_counter()
            try:
                s.sendto(msg.encode(), (host, port))
                resp, _ = s.recvfrom(1024)
                rtt = (time.perf_counter() - t0) * 1000
                results.append((msg, resp.decode(), rtt, "OK"))
            except socket.timeout:
                results.append((msg, "", 2000.0, "TIMEOUT"))
            print(f"  [{results[-1][2]:.3f}ms] {msg!r} -> {results[-1][3]}")
    ok = [r for r in results if r[3] == "OK"]
    print(f"\n  RTT médio UDP: {sum(r[2] for r in ok)/len(ok):.3f} ms | {len(ok)}/{len(results)} entregues")


def run_test(server_fn, client_fn, label):
    print(f"\n{'='*50}\n  {label}\n{'='*50}")
    t = threading.Thread(target=server_fn, daemon=True)
    t.start()
    time.sleep(0.3)
    client_fn()


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"

    if mode == "tcp-server":
        tcp_server(host)
    elif mode == "tcp-client":
        tcp_client(host)
    elif mode == "udp-server":
        udp_server(host)
    elif mode == "udp-client":
        udp_client(host)
    else:
        run_test(tcp_server, tcp_client, "TCP")
        run_test(udp_server, udp_client, "UDP")
