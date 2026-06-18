
from scapy.all import sniff, TCP, IP, Raw

PORTA_SERVIDOR = 5050
TAMANHO_CABECALHO = 4

buffers = {}


def chave_fluxo(pacote):
    ip = pacote[IP]
    tcp = pacote[TCP]
    return (ip.src, tcp.sport, ip.dst, tcp.dport)


def processar_buffer(chave):
    buffer = buffers[chave]

    while True:
        if len(buffer) < TAMANHO_CABECALHO:
            break  

        tamanho_declarado = int.from_bytes(buffer[:TAMANHO_CABECALHO], byteorder="big")
        tamanho_total_esperado = TAMANHO_CABECALHO + tamanho_declarado

        if len(buffer) < tamanho_total_esperado:
            # Mensagem ainda incompleta: aguarda mais pacotes
            tamanho_recebido_parcial = len(buffer) - TAMANHO_CABECALHO
            print(
                f"[ANALISADOR] {chave[0]}:{chave[1]} -> {chave[2]}:{chave[3]} | "
                f"mensagem em andamento: declarado={tamanho_declarado} "
                f"recebido_parcial={tamanho_recebido_parcial} (aguardando mais dados)"
            )
            break

        conteudo = buffer[TAMANHO_CABECALHO:tamanho_total_esperado]
        tamanho_recebido = len(conteudo)
        inconsistente = tamanho_recebido != tamanho_declarado

        status = "INCONSISTENTE" if inconsistente else "OK"
        print(
            f"[ANALISADOR] {chave[0]}:{chave[1]} -> {chave[2]}:{chave[3]} | "
            f"declarado={tamanho_declarado} recebido={tamanho_recebido} | {status}"
        )

        buffer = buffer[tamanho_total_esperado:]
        buffers[chave] = buffer


def handler_pacote(pacote):
    if not pacote.haslayer(TCP) or not pacote.haslayer(Raw):
        return

    tcp = pacote[TCP]
    if tcp.sport != PORTA_SERVIDOR and tcp.dport != PORTA_SERVIDOR:
        return

    payload = bytes(pacote[Raw].load)
    if not payload:
        return

    chave = chave_fluxo(pacote)
    buffers.setdefault(chave, b"")
    buffers[chave] += payload

    processar_buffer(chave)


def main():
    print(f"[ANALISADOR] Capturando trafego na porta {PORTA_SERVIDOR}...")
    print("[ANALISADOR] Pressione Ctrl+C para parar.\n")
    sniff(filter=f"tcp port {PORTA_SERVIDOR}", prn=handler_pacote, store=False)


if __name__ == "__main__":
    main()