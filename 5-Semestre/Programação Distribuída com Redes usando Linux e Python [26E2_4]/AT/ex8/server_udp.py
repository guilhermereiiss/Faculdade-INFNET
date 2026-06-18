
import socket
import random

HOST = "127.0.0.1"
PORT = 6060


def send_with_loss(sock, mensagem_ack, endereco_cliente, probabilidade_perda=0.5):
    if random.random() < probabilidade_perda:
        return False
    sock.sendto(mensagem_ack.encode("utf-8"), endereco_cliente)
    return True


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as servidor:
        servidor.bind((HOST, PORT))
        print(f"[SERVIDOR] Escutando em {HOST}:{PORT} (simulando perda de ~50% dos ACKs)")
        print("[SERVIDOR] Pressione Ctrl+C para parar.\n")

        while True:
            dados, endereco_cliente = servidor.recvfrom(1024)
            mensagem = dados.decode("utf-8", errors="replace")
            print(f"[SERVIDOR] Mensagem recebida de {endereco_cliente}: {mensagem!r}")

            ack_texto = f"ACK: {mensagem}"
            ack_enviado = send_with_loss(servidor, ack_texto, endereco_cliente)

            if ack_enviado:
                print(f"[SERVIDOR] ACK enviado para {endereco_cliente}\n")
            else:
                print(f"[SERVIDOR] ACK DESCARTADO (perda simulada) para {endereco_cliente}\n")


if __name__ == "__main__":
    main()