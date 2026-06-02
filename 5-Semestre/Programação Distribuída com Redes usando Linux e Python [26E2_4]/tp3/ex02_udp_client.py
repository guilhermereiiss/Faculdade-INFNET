import socket
import random
import string
import time

SERVER_HOST = "127.0.0.1"   
SERVER_PORT = 9000
BUFFER_SIZE = 4096
NUM_MENSAGENS = 10


def gerar_conteudo(tamanho: int) -> str:
    return "".join(random.choices(string.ascii_letters + string.digits, k=tamanho))


def cliente_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.settimeout(2.0)   

        print(f"[CLIENTE] Enviando {NUM_MENSAGENS} mensagens para {SERVER_HOST}:{SERVER_PORT}")
        print("-" * 60)

        for seq in range(1, NUM_MENSAGENS + 1):
            tamanho = random.randint(10, 2000)
            conteudo = gerar_conteudo(tamanho)
            mensagem = f"{seq} - {conteudo}"
            dados = mensagem.encode("utf-8")

            print(f"[ENVIANDO #{seq}] tamanho={len(dados)} bytes")
            s.sendto(dados, (SERVER_HOST, SERVER_PORT))
            time.sleep(0.05)  

            try:
                resposta, _ = s.recvfrom(BUFFER_SIZE)
                print(f"[ECHO    #{seq}] {resposta[:60].decode()}...")
            except socket.timeout:
                print(f"[TIMEOUT #{seq}] Sem resposta do servidor.")

        print("-" * 60)

if __name__ == "__main__":
    cliente_udp()
