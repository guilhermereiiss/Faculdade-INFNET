import sys
import dns.resolver


def resolver_registros(dominio):
    ips_a = []
    ips_aaaa = []

    try:
        respostas_a = dns.resolver.resolve(dominio, "A")
        ips_a = [r.address for r in respostas_a]
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        print(f"Erro: dominio '{dominio}' nao existe (NXDOMAIN).")
        sys.exit(1)

    try:
        respostas_aaaa = dns.resolver.resolve(dominio, "AAAA")
        ips_aaaa = [r.address for r in respostas_aaaa]
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        pass

    return ips_a, ips_aaaa


def main():
    if len(sys.argv) != 2:
        print("Uso: python3 resolve_dns.py <dominio>")
        sys.exit(1)

    dominio = sys.argv[1]
    ips_a, ips_aaaa = resolver_registros(dominio)

    print("=" * 50)
    print(f"RESOLUCAO DNS PARA: {dominio}")
    print("=" * 50)

    print(f"\nRegistros A (IPv4) encontrados: {len(ips_a)}")
    for ip in ips_a:
        print(f"  {ip}")

    print(f"\nRegistros AAAA (IPv6) encontrados: {len(ips_aaaa)}")
    for ip in ips_aaaa:
        print(f"  {ip}")


if __name__ == "__main__":
    main()