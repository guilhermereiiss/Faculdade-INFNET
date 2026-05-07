from routerTrie import RouterTrie

def main():
    router = RouterTrie()

    routes = [
        ("192.168.0.0/16", 10),
        ("192.168.1.0/24", 20),
        ("192.168.1.128/25", 30),
        ("10.0.0.0/8", 40),
        ("0.0.0.0/0", 50),
        ("2001:db8::/32", 100),
        ("2001:db8:a::/48", 200),
    ]

    print("=== Inserindo rotas ===")
    for cidr, rid in routes:
        router.insert(cidr, rid)
        print(f"[OK] Inserido: {cidr} -> ID {rid}")

    tests = [
        ("192.168.0.50", 10),
        ("192.168.1.20", 20),
        ("192.168.1.150", 30),
        ("10.255.0.1", 40),
        ("8.8.8.8", 50),
        ("2001:db8::1", 100),
        ("2001:db8:a:1::1", 200),
    ]

    print("\n=== Resultados dos Testes (LPM) ===")
    for ip, expected in tests:
        result = router.lookup(ip)
        status = "OK" if result == expected else "ERRO"
        print(f"{status:4} {ip:25} -> {result} (esperado: {expected})")


if __name__ == "__main__":
    main()