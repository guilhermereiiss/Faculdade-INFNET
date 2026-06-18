
import sys
import time
from collections import defaultdict
from scapy.all import sniff, TCP, IP, Raw

PORTA_SERVIDOR = 8080
ARQUIVO_LOG = "access.log"
LIMITE_ANOMALIA = 3

PATHS_VALIDOS = {"/home.html", "/contato.html"}


def handler_pacote_http(pacote):

    if not pacote.haslayer(TCP) or not pacote.haslayer(Raw):
        return

    tcp = pacote[TCP]
    if tcp.dport != PORTA_SERVIDOR:
        return  

    payload = bytes(pacote[Raw].load)
    primeira_linha = payload.split(b"\r\n", 1)[0].decode("utf-8", errors="replace")

    if primeira_linha.startswith(("GET ", "POST ", "PUT ", "DELETE ", "HEAD ")):
        ip_origem = pacote[IP].src
        print(f"[CAPTURA] {ip_origem} -> {primeira_linha}")


def analisar_log_para_anomalias(caminho_log=ARQUIVO_LOG):
    contagem_por_ip = defaultdict(int)
    detalhes_por_ip = defaultdict(list)

    try:
        with open(caminho_log, "r") as f:
            linhas = f.readlines()
    except FileNotFoundError:
        print(f"[ANALISADOR] Arquivo de log '{caminho_log}' nao encontrado ainda.")
        return

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        partes = linha.split("\t")
        if len(partes) != 5:
            continue
        timestamp, ip, metodo, endpoint, status = partes

        if endpoint not in PATHS_VALIDOS:
            contagem_por_ip[ip] += 1
            detalhes_por_ip[ip].append((timestamp, endpoint, status))

    print("\n" + "=" * 60)
    print("ANALISE DE PADRAO ANOMALO (path invalido por IP)")
    print("=" * 60)

    encontrou_anomalia = False
    for ip, contagem in contagem_por_ip.items():
        if contagem >= LIMITE_ANOMALIA:
            encontrou_anomalia = True
            print(f"\n[ANOMALIA DETECTADA] IP {ip} acessou path invalido {contagem} vezes:")
            for timestamp, endpoint, status in detalhes_por_ip[ip]:
                print(f"    {timestamp} | {endpoint} | status {status}")
        else:
            print(f"\n[OK] IP {ip} acessou path invalido {contagem} vez(es) (abaixo do limite de {LIMITE_ANOMALIA})")

    if not encontrou_anomalia:
        print("\nNenhum padrao anomalo encontrado no log atual.")


def main():
    print(f"[ANALISADOR] Capturando trafego HTTP na porta {PORTA_SERVIDOR}...")
    print("[ANALISADOR] Pressione Ctrl+C para parar a captura e analisar o log.\n")
    try:
        sniff(filter=f"tcp port {PORTA_SERVIDOR}", prn=handler_pacote_http, store=False)
    except KeyboardInterrupt:
        pass

    analisar_log_para_anomalias()


if __name__ == "__main__":
    main()

