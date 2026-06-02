import socket
import time
import errno

ALVOS = [
    ("127.0.0.1", 80,    "Porta 80   (HTTP padrão — pode estar aberta ou fechada)"),
    ("127.0.0.1", 9001,  "Porta 9001 (exercício 3 — aberta se servidor estiver rodando)"),
    ("127.0.0.1", 9999,  "Porta 9999 (alta, geralmente fechada)"),
    ("127.0.0.1", 22,    "Porta 22   (SSH — porta do sistema)"),
    ("127.0.0.1", 12345, "Porta 12345 (exercício 1 — provavelmente fechada)"),
]

TIMEOUT = 1.0   


def diagnosticar_porta(host: str, porta: int, descricao: str):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)

    inicio = time.monotonic()
    codigo = s.connect_ex((host, porta))
    elapsed = time.monotonic() - inicio

    s.close()

    if codigo == 0:
        estado = "ABERTA"
        interpretacao = "Conexão TCP bem-sucedida (SYN-ACK recebido)."
    elif codigo in (errno.ECONNREFUSED, 111):   
        estado = "FECHADA/RECUSADA"
        interpretacao = "RST recebido; porta ativa mas sem serviço escutando."
    elif codigo in (errno.ETIMEDOUT, 110, errno.EAGAIN):
        estado = "FILTRADA/TIMEOUT"
        interpretacao = "Sem resposta; firewall pode estar descartando pacotes silenciosamente."
    else:
        estado = f"CÓDIGO {codigo}"
        interpretacao = errno.errorcode.get(codigo, "Erro desconhecido.")

    print(f"\n  Alvo      : {descricao}")
    print(f"  Endereço  : {host}:{porta}")
    print(f"  Estado    : {estado}")
    print(f"  Código    : {codigo}")
    print(f"  Tempo     : {elapsed:.3f}s")
    print(f"  Diagnóstico: {interpretacao}")


print("=" * 65)
print("DIAGNÓSTICO DE PORTAS COM connect_ex()")
print("=" * 65)

for host, porta, descricao in ALVOS:
    diagnosticar_porta(host, porta, descricao)


