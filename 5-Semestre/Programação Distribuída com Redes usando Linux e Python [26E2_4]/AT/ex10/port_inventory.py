
import nmap
import subprocess

HOST_ALVO = "127.0.0.1"
PORTAS_VARREDURA = "1-1024"

PORTAS_SENSIVEIS = {
    21: "FTP — transferencia de arquivos sem criptografia",
    22: "SSH — acesso remoto; exposto em todas as interfaces (0.0.0.0)",
    23: "Telnet — acesso remoto sem criptografia",
    25: "SMTP — servidor de e-mail",
    80: "HTTP — servidor web sem criptografia",
    443: "HTTPS — servidor web",
    3306: "MySQL — banco de dados",
    5432: "PostgreSQL — banco de dados",
    6379: "Redis — banco de dados em memoria, sem autenticacao por padrao",
    8080: "HTTP alternativo — servidor web de desenvolvimento",
    27017: "MongoDB — banco de dados",
}


def varrer_portas(host, portas):
    print(f"[NMAP] Varrendo {host} nas portas {portas}...\n")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=host, ports=portas, arguments="-sV")  
    return scanner


def exibir_resultado_nmap(scanner, host):
    print("=" * 60)
    print("RESULTADO DA VARREDURA (python-nmap)")
    print("=" * 60)

    portas_abertas = []

    if host not in scanner.all_hosts():
        print(f"Host {host} nao respondeu ou nenhuma porta foi encontrada.")
        return portas_abertas

    for proto in scanner[host].all_protocols():
        portas = sorted(scanner[host][proto].keys())
        for porta in portas:
            info = scanner[host][proto][porta]
            estado = info["state"]
            servico = info["name"] or "desconhecido"
            versao = info.get("version", "")
            produto = info.get("product", "")
            descricao_servico = f"{produto} {versao}".strip() or servico

            print(f"  Porta {porta}/{proto:<4} | Estado: {estado:<6} | Servico: {descricao_servico}")

            if estado == "open":
                portas_abertas.append(porta)

    print()
    return portas_abertas


def verificar_porta_com_ss(portas):
    print("=" * 60)
    print("VERIFICACAO COM SS (duas portas detectadas)")
    print("=" * 60)

    portas_verificar = portas[:2]
    if not portas_verificar:
        print("Nenhuma porta aberta encontrada para verificar com ss.")
        return

    for porta in portas_verificar:
        print(f"\n[SS] Estado da porta {porta}:")
        resultado = subprocess.run(
            ["ss", "-tlnp", f"sport = :{porta}"],
            capture_output=True,
            text=True
        )
        saida = resultado.stdout.strip()
        if saida:
            print(saida)
        else:
            print(f"  Nenhuma informacao retornada pelo ss para a porta {porta}.")


def analisar_exposicao(portas_abertas):
    print("\n" + "=" * 60)
    print("ANALISE DE EXPOSICAO E MITIGACAO")
    print("=" * 60)

    encontrou = False
    for porta in portas_abertas:
        if porta in PORTAS_SENSIVEIS:
            encontrou = True
            print(f"\n[ATENCAO] Porta {porta} aberta — {PORTAS_SENSIVEIS[porta]}")
            print(f"  Justificativa: esta porta exposta localmente pode ser acessada")
            print(f"  por qualquer processo ou usuario do sistema, e se o servico")
            print(f"  estiver mal configurado, pode virar vetor de ataque interno.")
            print(f"  Mitigacao: se o servico nao for necessario, desative-o com")
            print(f"  'sudo systemctl stop <servico> && sudo systemctl disable <servico>'.")
            print(f"  Se for necessario, restrinja o acesso via firewall:")
            print(f"  'sudo ufw deny {porta}' ou configure o bind para 127.0.0.1 apenas.")

    if not encontrou:
        print("\nNenhuma porta sensivelmente exposta detectada nas portas abertas.")


def main():
    scanner = varrer_portas(HOST_ALVO, PORTAS_VARREDURA)
    portas_abertas = exibir_resultado_nmap(scanner, HOST_ALVO)
    verificar_porta_com_ss(portas_abertas)
    analisar_exposicao(portas_abertas)


if __name__ == "__main__":
    main()