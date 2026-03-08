import time
import resource
from collections import deque

def get_memoria_mb():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0

with open('lista_de_arquivos.txt', 'r') as f:
    files = [line.strip() for line in f.readlines()]

n = len(files)
print(f"Total de arquivos: {n}")

posicoes = [1, 100, 1000, 5000, n]          
indices = [0 if p == 1 else (n-1 if p == n else p-1) for p in posicoes]

# HASHTABLE
start_t = time.time()
start_m = get_memoria_mb()
hashtable = {i: files[i] for i in range(n)}
print(f"HASHTABLE (dict):")
print(f"Tempo armazenar: {time.time()-start_t:.6f} s | Memória: {get_memoria_mb()-start_m:.2f} MB")

start_t = time.time()
nomes_ht = [hashtable[idx] for idx in indices]
print(f"Tempo acessar 5 posições: {time.time()-start_t:.6f} s")
for p, nome in zip(posicoes, nomes_ht):
    print(f"  Posição {p:4d} → {nome}")

start_t = time.time()
hashtable[n] = "novo_arquivo_adicionado.txt"
print(f"Tempo adicionar: {time.time()-start_t:.6f} s")

start_t = time.time()
del hashtable[0]
print(f"Tempo remover: {time.time()-start_t:.6f} s")

# PILHA (list)
start_t = time.time()
start_m = get_memoria_mb()
pilha = files[:]
print(f"PILHA (list):")
print(f"Tempo armazenar: {time.time()-start_t:.6f} s | Memória: {get_memoria_mb()-start_m:.2f} MB")

start_t = time.time()
nomes_pilha = [pilha[idx] for idx in indices]
print(f"Tempo acessar 5 posições: {time.time()-start_t:.6f} s")
for p, nome in zip(posicoes, nomes_pilha):
    print(f"  Posição {p:4d} → {nome}")

start_t = time.time()
pilha.append("novo_arquivo_adicionado.txt")
print(f"Tempo adicionar (push): {time.time()-start_t:.6f} s")

start_t = time.time()
pilha.pop()
print(f"Tempo remover (pop): {time.time()-start_t:.6f} s")

# FILA (deque)
start_t = time.time()
start_m = get_memoria_mb()
fila = deque(files)
print(f"FILA (deque):")
print(f"Tempo armazenar: {time.time()-start_t:.6f} s | Memória: {get_memoria_mb()-start_m:.2f} MB")

start_t = time.time()
nomes_fila = [fila[idx] for idx in indices]
print(f"Tempo acessar 5 posições: {time.time()-start_t:.6f} s")
for p, nome in zip(posicoes, nomes_fila):
    print(f"  Posição {p:4d} → {nome}")

start_t = time.time()
fila.append("novo_arquivo_adicionado.txt")
print(f"Tempo adicionar (enqueue): {time.time()-start_t:.6f} s")

start_t = time.time()
fila.popleft()
print(f"Tempo remover (dequeue): {time.time()-start_t:.6f} s")
