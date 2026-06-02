
import socket

SERVER_HOST = "0.0.0.0" 
SERVER_PORT = 9000
BUFFER_SIZE = 4096


def servidor_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((SERVER_HOST, SERVER_PORT))
        print(f"[SERVIDOR] Escutando UDP em {SERVER_HOST}:{SERVER_PORT}")
        print("-" * 50)

        while True:
            try:
                dados, endereco = s.recvfrom(BUFFER_SIZE)
                ip_origem, porta_origem = endereco
                payload = dados.decode("utf-8", errors="replace")
                tamanho = len(dados)

                print(f"[RECEBIDO] IP origem  : {ip_origem}")
                print(f"           Porta orig.: {porta_origem}")
                print(f"           Tamanho    : {tamanho} bytes")
                print(f"           Conteúdo   : {payload}")
                print("-" * 50)

                s.sendto(dados, endereco)

            except KeyboardInterrupt:
                print("\n[SERVIDOR] Encerrando.")
                break


if __name__ == "__main__":
    servidor_udp()
