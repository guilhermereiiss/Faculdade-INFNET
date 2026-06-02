import ssl
import socket
import datetime

HOST = "www.google.com"
PORT = 443


def formatar_validade(timestamp: str) -> str:
    """Converte string de data do certificado para legível."""
    try:
        dt = datetime.datetime.strptime(timestamp, "%b %d %H:%M:%S %Y %Z")
        return dt.strftime("%d/%m/%Y %H:%M:%S UTC")
    except Exception:
        return timestamp


def inspecionar_tls(host: str, porta: int):
    ctx = ssl.create_default_context()

    with socket.create_connection((host, porta), timeout=5) as sock:
        with ctx.wrap_socket(sock, server_hostname=host) as tls_sock:

            versao_tls = tls_sock.version()
            cipher_info = tls_sock.cipher()    

            cert = tls_sock.getpeercert()
            cert_pem = ssl.DER_cert_to_PEM_cert(
                tls_sock.getpeercert(binary_form=True)
            )

            print("=" * 65)
            print(f"HOST          : {host}:{porta}")
            print("=" * 65)

            # Subject
            subject = dict(x[0] for x in cert.get("subject", []))
            print(f"\n── SUBJECT ─────────────────────────────────────────────")
            for k, v in subject.items():
                print(f"  {k:<25}: {v}")

            # Issuer
            issuer = dict(x[0] for x in cert.get("issuer", []))
            print(f"\n── ISSUER ──────────────────────────────────────────────")
            for k, v in issuer.items():
                print(f"  {k:<25}: {v}")

            # Validade
            not_before = formatar_validade(cert.get("notBefore", ""))
            not_after  = formatar_validade(cert.get("notAfter",  ""))
            print(f"\n── VALIDADE ────────────────────────────────────────────")
            print(f"  Válido desde : {not_before}")
            print(f"  Válido até   : {not_after}")

            # TLS
            print(f"\n── TLS ─────────────────────────────────────────────────")
            print(f"  Versão TLS   : {versao_tls}")
            print(f"  Cipher suite : {cipher_info[0]}")
            print(f"  Protocolo    : {cipher_info[1]}")
            print(f"  Tamanho chave: {cipher_info[2]} bits")

            sans = [v for t, v in cert.get("subjectAltName", []) if t == "DNS"]
            if sans:
                print(f"\n── SUBJECT ALT NAMES ───────────────────────────────────")
                for san in sans[:10]:
                    print(f"  {san}")

            print(f"\n── CERTIFICADO PEM ─────────────────────────────────────")
            print(cert_pem[:500] + "... [truncado]")
            print("=" * 65)

if __name__ == "__main__":
    inspecionar_tls(HOST, PORT)
