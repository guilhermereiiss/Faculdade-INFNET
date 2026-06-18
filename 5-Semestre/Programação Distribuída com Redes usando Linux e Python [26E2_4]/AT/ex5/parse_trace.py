

import sys
import re


def parse_trace(caminho_arquivo):
    with open(caminho_arquivo, "r", errors="replace") as f:
        linhas = f.readlines()

    metodo = None
    host = None
    status_code = None
    ip_remoto = None
    headers_enviados = []
    headers_recebidos = []

    secao_atual = None  

    for linha in linhas:
        linha = linha.rstrip("\n")

    
        if ("Connected to" in linha or "Established connection to" in linha) and "port" in linha:
            m = re.search(r"to .*?\(([\w.:]+?)\)? ?port\s*\d", linha)
            if m:
                ip_remoto = m.group(1).strip()
            continue

        if linha.startswith("== Info:"):
            continue

        if linha.startswith("=> Send header"):
            secao_atual = "send_header"
            continue
        if linha.startswith("=> Send data"):
            secao_atual = "send_data"
            continue

        if linha.startswith("<= Recv header"):
            secao_atual = "recv_header"
            continue
        if linha.startswith("<= Recv data"):
            secao_atual = "recv_data"  
            continue

        if linha.startswith("==") or linha.startswith("* "):
            secao_atual = None
            continue

        m = re.match(r"^[0-9a-fA-F]{4,8}:\s?(.*)$", linha)
        if not m or secao_atual is None:
            continue

        conteudo = m.group(1)

        if secao_atual == "send_header":
            m_metodo = re.match(r"^([A-Z]+)\s+(\S+)\s+HTTP/[\d.]+", conteudo)
            if m_metodo:
                metodo = m_metodo.group(1)
            elif conteudo.lower().startswith("host:"):
                host = conteudo.split(":", 1)[1].strip()
            if conteudo.strip():
                headers_enviados.append(conteudo)

        elif secao_atual == "recv_header":
            m_status = re.match(r"^HTTP/[\d.]+\s+(\d+)", conteudo)
            if m_status:
                status_code = m_status.group(1)
            elif conteudo.strip():
                headers_recebidos.append(conteudo)

    return {
        "metodo": metodo,
        "host": host,
        "status_code": status_code,
        "ip_remoto": ip_remoto,
        "headers_enviados": headers_enviados,
        "headers_recebidos": headers_recebidos,
    }


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 parse_trace.py <arquivo_trace.txt>")
        sys.exit(1)

    caminho = sys.argv[1]
    dados = parse_trace(caminho)

    print("=" * 50)
    print("RESUMO DO TRACE HTTP")
    print("=" * 50)
    print(f"Metodo HTTP    : {dados['metodo']}")
    print(f"Host           : {dados['host']}")
    print(f"Status code    : {dados['status_code']}")
    print(f"IP remoto      : {dados['ip_remoto']}")
    print()
    print("-- Headers enviados (requisicao) --")
    for h in dados["headers_enviados"]:
        print(f"  {h}")
    print()
    print("-- Headers recebidos (resposta) --")
    for h in dados["headers_recebidos"]:
        print(f"  {h}")


if __name__ == "__main__":
    main()