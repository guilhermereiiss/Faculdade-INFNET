
import socket
import sys
import time
import threading
import subprocess
import shutil
import datetime

PORT = 23000
IAC = 255; WILL = 251; WONT = 252; DO = 253; DONT = 254; SB = 250; SE = 240


def _now():
    return datetime.datetime.now().strftime("%H:%M:%S")


def strip_iac(data):
    result = bytearray()
    i = 0
    while i < len(data):
        if data[i] == IAC:
            cmd = data[i+1] if i+1 < len(data) else 0
            if cmd in (WILL, WONT, DO, DONT):
                i += 3
            elif cmd == SB:
                end = data.find(bytes([IAC, SE]), i+2)
                i = end + 2 if end != -1 else len(data)
            else:
                i += 2
        else:
            result.append(data[i])
            i += 1
    return bytes(result)


def handle_client(conn, addr):
    try:
        conn.sendall(bytes([IAC, WILL, 3, IAC, WILL, 1]))
        conn.sendall(b"Bem-vindo! Comandos: help, date, echo <msg>, quit\r\n> ")
        buf = b""
        while True:
            data = conn.recv(256)
            if not data:
                break
            buf += strip_iac(data)
            while b"\r\n" in buf or (b"\r" in buf and b"\n" in buf):
                for sep in (b"\r\n", b"\n", b"\r"):
                    if sep in buf:
                        line, _, buf = buf.partition(sep)
                        break
                cmd = line.decode("utf-8", errors="ignore").strip()
                if not cmd:
                    conn.sendall(b"> ")
                    continue
                parts = cmd.split(maxsplit=1)
                verb = parts[0].lower()
                if verb == "help":
                    r = "Comandos: help | date | echo <msg> | quit"
                elif verb == "date":
                    r = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                elif verb == "echo":
                    r = parts[1] if len(parts) > 1 else ""
                elif verb == "quit":
                    conn.sendall(b"Tchau!\r\n")
                    return
                else:
                    r = f"Desconhecido: '{cmd}'"
                conn.sendall((r + "\r\n> ").encode())
    except (ConnectionResetError, BrokenPipeError):
        pass
    finally:
        conn.close()


def telnet_server(host="0.0.0.0", port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        print(f"[{_now()}] Servidor Telnet em {host}:{port}")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()


def read_until(s, marker=b"> ", timeout=2.0):
    s.settimeout(timeout)
    buf = b""
    try:
        while marker not in buf:
            chunk = s.recv(256)
            if not chunk:
                break
            buf += chunk
    except socket.timeout:
        pass
    clean = bytearray()
    i = 0
    while i < len(buf):
        b = buf[i]
        if b == IAC:
            cmd = buf[i+1] if i+1 < len(buf) else 0
            i += 3 if cmd in (WILL, WONT, DO, DONT) else 2
        elif b not in (0, 13):
            clean.append(b)
            i += 1
        else:
            i += 1
    return clean.decode("utf-8", errors="ignore")


def telnet_client(host="127.0.0.1", port=PORT, test=False):
    cmds = ["help", "date", "echo Olá Telnet!", "echo Teste", "invalido", "quit"]
    results = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        read_until(s)
        if not test:
            print(f"Conectado a {host}:{port}. Digite comandos (quit para sair).")
            for cmd in input().split("\n") if False else cmds:
                pass
        for cmd in cmds:
            s.sendall((cmd + "\r\n").encode())
            t0 = time.perf_counter()
            resp = read_until(s)
            rtt = (time.perf_counter() - t0) * 1000
            results.append((cmd, resp.strip(), rtt))
            print(f"  [{rtt:.2f}ms] {cmd!r} -> {resp.strip()[:60]!r}")
            if cmd == "quit":
                break

    print(f"\n  RTT médio: {sum(r[2] for r in results)/len(results):.2f} ms | {len(results)} testes")


def curl_analysis(host="127.0.0.1", port=PORT):
    if not shutil.which("curl"):
        print("curl não encontrado. Instale com: sudo apt install curl")
        return
    tests = [("Conexão simples", ""), ("Comando help", "help\r\n"),
             ("Comando date", "date\r\n"), ("Comando echo", "echo Teste curl\r\n"),
             ("Quit", "quit\r\n")]
    print(f"\n{'='*50}\n  Análise curl -> {host}:{port}\n{'='*50}")
    for desc, data in tests:
        cmd = ["curl", "--silent", "--max-time", "3", "--data-binary", data,
               f"telnet://{host}:{port}"]
        t0 = time.perf_counter()
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=5)
            lat = (time.perf_counter() - t0) * 1000
            out = "".join(c for c in r.stdout.decode("utf-8", errors="ignore") if c.isprintable())[:60]
            status = "OK" if r.returncode == 0 else f"ERR({r.returncode})"
        except subprocess.TimeoutExpired:
            lat, out, status = 3000.0, "(timeout)", "TIMEOUT"
        print(f"  {status:>8} [{lat:>7.2f}ms] {desc}: {out!r}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    host = sys.argv[2] if len(sys.argv) > 2 else "127.0.0.1"

    if mode == "server":
        telnet_server(host)
    elif mode == "client":
        telnet_client(host, test=False)
    elif mode == "curl":
        curl_analysis(host)
    else:
        t = threading.Thread(target=telnet_server, args=(host,), daemon=True)
        t.start()
        time.sleep(0.3)
        telnet_client(host, test=True)
        curl_analysis(host)
