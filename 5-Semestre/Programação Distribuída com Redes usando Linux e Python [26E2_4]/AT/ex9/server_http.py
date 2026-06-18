import socket
import datetime

HOST = "127.0.0.1"
PORT = 8080
ARQUIVO_LOG = "access.log"

PATHS_VALIDOS = {"/home.html", "/contato.html"}

CONTEUDO = {
    "/home.html": {
        "pt": "<html><body><h1>Bem-vindo</h1><p>Esta e a pagina inicial.</p></body></html>",
        "en": "<html><body><h1>Welcome</h1><p>This is the home page.</p></body></html>",
    },
    "/contato.html": {
        "pt": "<html><body><h1>Contato</h1><p>Envie um e-mail para contato@exemplo.com.</p></body></html>",
        "en": "<html><body><h1>Contact</h1><p>Send an email to contato@exemplo.com.</p></body></html>",
    },
}


def registrar_log(ip, metodo, endpoint, status):
    timestamp = datetime.datetime.now().isoformat()
    linha = f"{timestamp}\t{ip}\t{metodo}\t{endpoint}\t{status}\n"
    with open(ARQUIVO_LOG, "a") as f:
        f.write(linha)


def escolher_idioma(accept_language_header):
    if not accept_language_header:
        return "en"
    header_lower = accept_language_header.lower()
    if "pt" in header_lower:
        return "pt"
    if "en" in header_lower:
        return "en"
    return "en"


def parse_requisicao(dados_brutos):
    try:
        texto = dados_brutos.decode("utf-8", errors="replace")
        linhas = texto.split("\r\n")
        linha_requisicao = linhas[0]
        partes = linha_requisicao.split(" ")
        if len(partes) != 3:
            return None
        metodo, path, versao = partes
        if not versao.startswith("HTTP/"):
            return None

        headers = {}
        for linha in linhas[1:]:
            if not linha or ":" not in linha:
                continue
            nome, _, valor = linha.partition(":")
            headers[nome.strip().lower()] = valor.strip()

        return {"metodo": metodo, "path": path, "headers": headers}
    except Exception:
        return None


def montar_resposta(status_code, status_texto, corpo, content_type="text/html"):
    corpo_bytes = corpo.encode("utf-8")
    linhas = [
        f"HTTP/1.1 {status_code} {status_texto}",
        f"Content-Type: {content_type}; charset=utf-8",
        f"Content-Length: {len(corpo_bytes)}",
        "Connection: close",
        "",
        "",
    ]
    cabecalho = "\r\n".join(linhas).encode("utf-8")
    return cabecalho + corpo_bytes


def tratar_requisicao(conexao, endereco_cliente):
    ip_cliente = endereco_cliente[0]
    try:
        dados = conexao.recv(4096)
        if not dados:
            return

        requisicao = parse_requisicao(dados)

        if requisicao is None:
            resposta = montar_resposta(400, "Bad Request", "<html><body><h1>400 Bad Request</h1></body></html>")
            conexao.sendall(resposta)
            registrar_log(ip_cliente, "?", "?", 400)
            return

        metodo = requisicao["metodo"]
        path = requisicao["path"]
        headers = requisicao["headers"]

        if metodo != "GET":
            resposta = montar_resposta(405, "Method Not Allowed", "<html><body><h1>405 Method Not Allowed</h1></body></html>")
            conexao.sendall(resposta)
            registrar_log(ip_cliente, metodo, path, 405)
            return

        if path not in PATHS_VALIDOS:
            resposta = montar_resposta(404, "Not Found", "<html><body><h1>404 Not Found</h1></body></html>")
            conexao.sendall(resposta)
            registrar_log(ip_cliente, metodo, path, 404)
            return

        idioma = escolher_idioma(headers.get("accept-language"))
        corpo = CONTEUDO[path][idioma]
        resposta = montar_resposta(200, "OK", corpo)
        conexao.sendall(resposta)
        registrar_log(ip_cliente, metodo, path, 200)

    finally:
        conexao.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        servidor.bind((HOST, PORT))
        servidor.listen(5)
        print(f"[SERVIDOR HTTP] Escutando em http://{HOST}:{PORT}")
        print(f"[SERVIDOR HTTP] Log de acessos em: {ARQUIVO_LOG}")
        print("[SERVIDOR HTTP] Pressione Ctrl+C para parar.\n")

        while True:
            conexao, endereco = servidor.accept()
            tratar_requisicao(conexao, endereco)


if __name__ == "__main__":
    main()