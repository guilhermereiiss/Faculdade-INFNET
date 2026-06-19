
from scapy.all import ARP, Ether, srp, sniff, conf
import sys

REDE = "10.0.2.0/24"
GATEWAY = "10.0.2.2"
LIMITE_IPS_POR_MAC = 3

ip_para_mac = {}
mac_para_ips = {}

def escanear():
    print(f"[*] escaneando {REDE}...")
    pacote = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=REDE)
    respostas, _ = srp(pacote, timeout=3, verbose=False)

    tabela = {}
    for enviado, recebido in respostas:
        tabela[recebido.psrc] = recebido.hwsrc.lower()
    return tabela


def mostra_tabela(tabela):
    print()
    for ip in sorted(tabela, key=lambda x: list(map(int, x.split('.')))):
        marca = " <- gateway" if ip == GATEWAY else ""
        print(f"{ip:<16} {tabela[ip]}{marca}")
    print(f"\n{len(tabela)} dispositivos encontrados")


def checa_pacote(pkt, mac_gateway_real):
    if not (pkt.haslayer(ARP) and pkt[ARP].op == 2):
        return

    ip = pkt[ARP].psrc
    mac = pkt[ARP].hwsrc.lower()

    if ip == GATEWAY and mac != mac_gateway_real:
        print(f"\n[ALERTA] o gateway {GATEWAY} apareceu com um MAC diferente!")
        print(f"  mac real: {mac_gateway_real}")
        print(f"  mac visto agora: {mac}")
        print("  isso pode ser um ataque de ARP spoofing / MITM")

    if ip in ip_para_mac and ip_para_mac[ip] != mac:
        print(f"\n[suspeito] o IP {ip} mudou de MAC ({ip_para_mac[ip]} -> {mac})")

    mac_para_ips.setdefault(mac, set()).add(ip)
    if len(mac_para_ips[mac]) > LIMITE_IPS_POR_MAC:
        print(f"\n[suspeito] o MAC {mac} esta respondendo por {len(mac_para_ips[mac])} IPs diferentes: {mac_para_ips[mac]}")


if __name__ == "__main__":
    tabela = escanear()

    if not tabela:
        print("nenhum host respondeu")
        print("dicas: confere se o Npcap esta instalado, se esta rodando como admin")
        print("       e se a faixa REDE esta correta pra sua rede")
        sys.exit(1)

    ip_para_mac = tabela
    mostra_tabela(tabela)

    mac_gateway = tabela.get(GATEWAY, "desconhecido")
    if GATEWAY not in tabela:
        print(f"aviso: gateway {GATEWAY} nao apareceu no scan")

    print("\nmonitorando ARP, ctrl+c pra sair...\n")
    try:
        sniff(filter="arp", prn=lambda p: checa_pacote(p, mac_gateway), store=0)
    except KeyboardInterrupt:
        print("\nencerrado")
