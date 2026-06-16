# sniffer.py
# pip install pcapy-ng
# precisa rodar com sudo / admin

import pcapy
import struct

INTERFACE = 'lo'  # no mac eh 'lo0', no windows usa o nome da interface do Npcap
PORTA = 8443
FILTRO = f"tcp port {PORTA}"
PALAVRAS_CHAVE = ["AUTH_TOKEN", "REBOOT_SERVER"]


def le_ip(pacote):
    if len(pacote) < 20:
        return None, None
    ihl = (pacote[0] & 0x0F) * 4
    protocolo = pacote[9]
    return protocolo, pacote[ihl:]


def le_tcp(pacote):
    if len(pacote) < 20:
        return None, None, None
    porta_origem = struct.unpack('!H', pacote[0:2])[0]
    porta_destino = struct.unpack('!H', pacote[2:4])[0]
    offset = ((pacote[12] >> 4) & 0xF) * 4
    return porta_origem, porta_destino, pacote[offset:]


def texto_legivel(dados):
    s = ''
    for b in dados:
        s += chr(b) if 32 <= b < 127 else '.'
    return s


def hex_legivel(dados):
    return ''.join(f'\\x{b:02x}' for b in dados)


def trata_pacote(header, pacote):
    # pacote de loopback no linux vem com 4 bytes extra antes do IP
    payload_ip = pacote[4:] if len(pacote) > 4 else pacote

    protocolo, payload_tcp = le_ip(payload_ip)
    if protocolo != 6:  # so interessa TCP
        return

    porta_o, porta_d, payload = le_tcp(payload_tcp)
    if porta_o != PORTA and porta_d != PORTA:
        return

    print(f"\n[+] Pacote TCP Capturado! Tamanho: {len(pacote)} bytes.")

    if not payload:
        return

    trecho = payload[:80]
    print(f"[Dados Brutos do Payload]: {hex_legivel(trecho)}")
    print(f"[Texto Convertido]: {texto_legivel(trecho)}")

    achou = False
    for palavra in PALAVRAS_CHAVE:
        if palavra.encode() in payload:
            achou = True
            print(f"[!!!] '{palavra}' apareceu em texto claro, algo ta errado")

    if not achou:
        print("[-] Alerta: Padrao 'AUTH_TOKEN' NAO encontrado. Os dados estao devidamente cifrados via TLS.")


print(f"[*] Iniciando captura na interface {INTERFACE} (Porta {PORTA})...")

cap = pcapy.open_live(INTERFACE, 65535, True, 1000)
cap.setfilter(FILTRO)

try:
    while True:
        header, pacote = cap.next()
        if pacote:
            trata_pacote(header, pacote)
except KeyboardInterrupt:
    print("\n[*] captura parada")
