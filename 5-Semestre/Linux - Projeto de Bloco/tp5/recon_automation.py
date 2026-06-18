
import subprocess
import json
import os
import sys

try:
    import nmap
except ImportError:
    print("falta instalar: pip install python-nmap")
    sys.exit(1)

ALVO_DNS  = "zonetransfer.me"
ALVO_NMAP = "scanme.nmap.org"
SAIDA     = "relatorio_recon.json"

TEMP = os.environ.get("TEMP", "C:\\Windows\\Temp")
DNS_STD_JSON   = os.path.join(TEMP, "dns_std.json")
DNS_BRUTE_JSON = os.path.join(TEMP, "dns_brute.json")

def achar_wordlist():
    possiveis = [
        os.path.join(os.environ.get("APPDATA", ""), "dnsrecon", "namelist.txt"),
        r"C:\dnsrecon\namelist.txt",
        r"C:\Tools\dnsrecon\namelist.txt",
    ]
    for p in possiveis:
        if os.path.exists(p):
            return p
    return None


def roda_dnsrecon(dominio):
    print(f"\n[*] rodando dnsrecon em {dominio}")
    resultado = {"dominio": dominio, "registros": [], "subdominios": [], "erro": None}

    try:
        subprocess.run(
            ["dnsrecon", "-d", dominio, "-t", "std", "--json", DNS_STD_JSON],
            capture_output=True, text=True, timeout=60
        )
        if os.path.exists(DNS_STD_JSON):
            with open(DNS_STD_JSON, encoding="utf-8") as f:
                resultado["registros"] = json.load(f)

    except FileNotFoundError:
        resultado["erro"] = "dnsrecon nao encontrado, tentando fallback com nslookup"
        print(f"  [aviso] {resultado['erro']}")
        resultado["registros"] = fallback_nslookup(dominio)

    except subprocess.TimeoutExpired:
        resultado["erro"] = "dnsrecon deu timeout"

    wordlist = achar_wordlist()
    if wordlist:
        print("  rodando brute force de subdominios...")
        try:
            subprocess.run(
                ["dnsrecon", "-d", dominio, "-t", "brt", "-D", wordlist, "--json", DNS_BRUTE_JSON],
                capture_output=True, text=True, timeout=120
            )
            if os.path.exists(DNS_BRUTE_JSON):
                with open(DNS_BRUTE_JSON, encoding="utf-8") as f:
                    brutos = json.load(f)
                    resultado["subdominios"] = [r for r in brutos if isinstance(r, dict) and r.get("type") == "A"]
        except Exception as e:
            resultado["subdominios"] = [{"erro": str(e)}]
    else:
        print("  wordlist nao encontrada, pulando brute force")

    return resultado


def fallback_nslookup(dominio):
    registros = []
    try:
        p = subprocess.run(["nslookup", dominio], capture_output=True, text=True, timeout=10)
        for linha in p.stdout.strip().splitlines():
            if "Address" in linha and "#" not in linha:
                ip = linha.split(":")[-1].strip()
                registros.append({"type": "A", "name": dominio, "address": ip})
    except Exception:
        pass

    for tipo in ["MX", "NS"]:
        try:
            p = subprocess.run(["nslookup", f"-type={tipo}", dominio], capture_output=True, text=True, timeout=10)
            for linha in p.stdout.strip().splitlines():
                if "mail exchanger" in linha.lower() or "nameserver" in linha.lower():
                    registros.append({"type": tipo, "name": dominio, "address": linha.strip()})
        except Exception:
            pass

    return registros


def roda_nmap(alvo):
    print(f"\n[*] rodando nmap em {alvo} (pode demorar um pouco)")
    nm = nmap.PortScanner()
    saida = {"alvo": alvo, "hosts": {}, "erro": None}

    try:
        nm.scan(hosts=alvo, arguments="--top-ports 100 -sV --script=vuln,discovery -Pn -T3")

        for host in nm.all_hosts():
            info = {"hostname": nm[host].hostname(), "estado": nm[host].state(), "portas": []}

            for proto in nm[host].all_protocols():
                for porta in sorted(nm[host][proto].keys()):
                    dados = nm[host][proto][porta]
                    if dados["state"] != "open":
                        continue
                    info["portas"].append({
                        "porta": porta,
                        "protocolo": proto.upper(),
                        "servico": dados.get("name", ""),
                        "produto": dados.get("product", ""),
                        "versao": dados.get("version", ""),
                        "scripts": dados.get("script", {})
                    })

            saida["hosts"][host] = info

    except Exception as e:
        saida["erro"] = str(e)
        print(f"  [erro] {e}")

    return saida


def imprime_relatorio(dns, nm):
    print("\n" + "=" * 50)
    print("RELATORIO AUTOMATIZADO DE SUPERFICIE DE ATAQUE")
    print("=" * 50)

    print(f"\n[+] alvo dns: {dns['dominio']}")
    if dns["erro"]:
        print(f"  aviso: {dns['erro']}")

    if dns["registros"]:
        print("\nregistros encontrados:")
        for r in dns["registros"][:15]:
            print(f"  - {r}")
    else:
        print("  nenhum registro encontrado")

    if dns["subdominios"]:
        print(f"\nsubdominios via brute force ({len(dns['subdominios'])}):")
        for s in dns["subdominios"][:10]:
            print(f"  * {s}")

    print(f"\n[+] varredura nmap em {nm['alvo']}")
    if nm["erro"]:
        print(f"  erro: {nm['erro']}")
    elif not nm["hosts"]:
        print("  nenhuma porta aberta / host nao respondeu")
    else:
        for ip, info in nm["hosts"].items():
            print(f"\nhost: {ip} ({info['hostname']})")
            if not info["portas"]:
                print("  sem portas abertas")
            for p in info["portas"]:
                servico = f"{p['produto']} {p['versao']}".strip() or p['servico']
                print(f"  porta {p['porta']}/{p['protocolo']} aberta - {servico}")
                for nome_script, txt in p["scripts"].items():
                    primeira_linha = txt.strip().splitlines()[0] if txt.strip() else ""
                    print(f"    [{nome_script}] {primeira_linha}")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    print("ATENCAO: usar so em alvos autorizados (zonetransfer.me / scanme.nmap.org)")

    resultado_dns  = roda_dnsrecon(ALVO_DNS)
    resultado_nmap = roda_nmap(ALVO_NMAP)

    imprime_relatorio(resultado_dns, resultado_nmap)

    relatorio = {"dns": resultado_dns, "nmap": resultado_nmap}
    with open(SAIDA, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, indent=2, ensure_ascii=False, default=str)

    print(f"\n[+] relatorio salvo em {SAIDA}")
