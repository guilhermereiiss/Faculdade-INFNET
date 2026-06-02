
import socket
import time

HOST    = "127.0.0.1"
PORTA_INICIO = 1
PORTA_FIM    = 1024      
TIMEOUT      = 0.3       
LOTE         = 50        


def varrer_portas(host: str, inicio: int, fim: int, timeout: float):
    abertas = []
    total = fim - inicio + 1

    print(f"[SCANNER] Varrendo {host} portas {inicio}–{fim} (timeout={timeout}s)")
    print(f"          Total de portas a testar: {total}")
    print("-" * 55)

    t_inicio = time.monotonic()

    for porta in range(inicio, fim + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        codigo = s.connect_ex((host, porta))
        s.close()

        if codigo == 0:
            abertas.append(porta)
            print(f"  [ABERTA] {host}:{porta}")

        # Progresso a cada LOTE portas
        if (porta - inicio + 1) % LOTE == 0:
            progresso = (porta - inicio + 1) / total * 100
            print(f"  [{progresso:5.1f}%] {porta - inicio + 1}/{total} portas verificadas...")

    t_total = time.monotonic() - t_inicio

    print("-" * 55)
    print(f"[SCANNER] Varredura concluída em {t_total:.2f}s")
    print(f"[SCANNER] Portas abertas encontradas ({len(abertas)}): {abertas}")
    return abertas, t_total

if __name__ == "__main__":
    varrer_portas(HOST, PORTA_INICIO, PORTA_FIM, TIMEOUT)
