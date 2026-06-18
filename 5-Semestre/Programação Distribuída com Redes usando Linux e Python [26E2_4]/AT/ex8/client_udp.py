
import socket
import time

HOST = "127.0.0.1"
PORT = 6060
TIMEOUT_SEGUNDOS = 1.0
MAX_TENTATIVAS = 6


def enviar_com_confirmacao(mensagem, host=HOST, porta=PORT):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIMEOUT_SEGUNDOS)

    tentativas_realizadas = 0
    sucesso = False

    try:
        for tentativa in range(1, MAX_TENTATIVAS + 1):
            tentativas_realizadas = tentativa
            print(f"[CLIENTE] Tentativa {tentativa}: enviando {mensagem!r} para {host}:{porta}")
            sock.sendto(mensagem.encode("utf-8"), (host, porta))

            try:
                dados, _ = sock.recvfrom(1024)
                resposta = dados.decode("utf-8", errors="replace")
                print(f"[CLIENTE] ACK recebido: {resposta!r}")
                sucesso = True
                break
            except socket.timeout:
                print(f"[CLIENTE] Timeout ({TIMEOUT_SEGUNDOS}s) sem receber ACK. Retransmitindo...")
                continue
    finally:
        sock.close()

    print()
    if sucesso:
        print(f"[CLIENTE] RESULTADO FINAL: sucesso apos {tentativas_realizadas} tentativa(s).")
    else:
        print(f"[CLIENTE] RESULTADO FINAL: falha apos {tentativas_realizadas} tentativas (sem ACK).")

    return sucesso, tentativas_realizadas


def main():
    enviar_com_confirmacao("Mensagem importante do cliente UDP")


if __name__ == "__main__":
    main()