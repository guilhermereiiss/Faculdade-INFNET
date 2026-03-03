#%% [markdown]
# # Exercício 1 - Classificar transações bancárias

#%% [code]

ANO_2_DIGITOS = 6

VALOR_TRANSACAO = 25000
TIPO_TRANSACAO = "transferência"
CODIGO_CLIENTE = "CL3805"

limite = 1000 * ANO_2_DIGITOS

if VALOR_TRANSACAO > limite and TIPO_TRANSACAO == "transferência":
    print("Alerta: verificar origem da transferência")
elif TIPO_TRANSACAO == "saque":
    print("Alerta: confirmar com o cliente")
else:
    print("Transação normal")


#%% [markdown]
# # Exercício 2 - Verificar elegibilidade para promoção

#%% [code]

tempo_empresa_anos = 3
nota_avaliacao = 8.5
carga_horaria = 40

if tempo_empresa_anos > 2 and nota_avaliacao >= 8.0:
    print("Elegível para promoção")
else:
    print("Aguardando próxima avaliação")

#%% [markdown]
# # Exercício 3 - Avaliar risco de atraso

#%% [code]

distancia_km = 350
clima = "chuva"
zona_entrega = "rural"

if (distancia_km > 300 and clima == "chuva") or zona_entrega == "rural":
    print("Risco alto de atraso")
else:
    print("Entrega dentro do previsto")


#%% [markdown]
# # Exercício 4 - Tratar falhas de sensores 

#%% [code]

codigo_falha ="F2"
temperatura = 65

if codigo_falha == "F1" and temperatura < 40:
    print("Reiniciar máquina")
elif codigo_falha == "F2" and temperatura > 60:
    print("Verificar conexão elétrica e sistema de refrigeração")
elif codigo_falha == "F3" and 45 <= temperatura <= 55:
    print("Ajustar temperatura da esteira")
elif codigo_falha == "F4":
    print("Realizar diagnóstico dos sensores ópticos")
elif codigo_falha in ["F1", "F2", "F3", "F4"]:
    print("Falha não reconhecida pelo sistema de alarme. Acionar engenheiro responsável")
else:
    print("Codigo não reconhecido")


#%% [markdown]
# # Exercício 5 - Filtrar clientes satisfeitos

#%% [code]
notas_avaliacao = [5, 8, 10, 6, 9, 4]

for nota in notas_avaliacao:
    if nota > 7:
        print(f"Nota: {nota}")


#%% [markdown]
# # Exercício 6 - Gerar lista de comissões

#%% [code]
comissoes = list(range(0, 51, 5))

print("Lista de comissões:", comissoes)


#%% [markdown]
# # Exercício 7 - Controlar tentativas de conexão

#%% [code]
tentativas_conexao = [False, False, False, True, True]

tentativas = 0
limite_tentativas = 3

i = 0

while i < len(tentativas_conexao):
    print("Tentando conectar...")
    tentativas += 1

    if tentativas_conexao[i]:
        print("Conexão concluida")
        break

    if tentativas == limite_tentativas:
        print("Conexão interrompida após limite de tentativas")
        break

    i += 1


#%% [markdown]
# # Exercício 8 - Reorganizar fila de pedidos

#%% [code]
# Cenário A (urgente): prioridade_urgente = True.

pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = True
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)  
else:
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
    else:
        print("Pedido a substituir não encontrado, mantendo a fila inalterada.")

print("Fila final (Cenário A):", pedidos)

# Cenário B (não urgente + substituição existe): prioridade_urgente = False e pedido_a_substituir está presente em pedidos.

pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = False
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
    else:
        print("Pedido a substituir não encontrado, mantendo a fila inalterada.")

print("Fila final (Cenário B):", pedidos)

# Cenário C (não urgente + substituição não existe): prioridade_urgente = False e pedido_a_substituir não está na lista; mantenha a lista inalterada e imprima uma mensagem explicativa antes da fila final.

pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P000"  
prioridade_urgente = False
pedido_urgente = "P999"

if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
    else:
        print("Pedido a substituir não encontrado, mantendo a fila inalterada.")

print("Fila final (Cenário C):", pedidos)

#%% [markdown]
# # Exercício 9 - Unificar estoque de armazéns

#%% [code]
produtos_a = ["banana", "maçã"]
produtos_b = ["laranja", "pera"]
produtos_c = ["laranja", "banana", "maçã", "romã"]

estoque_total = produtos_a + produtos_b + produtos_c

print("Estoque total:", estoque_total)

print("\nContagem dos produtos:")
for produto in set(estoque_total):
    print(f"{produto}: {estoque_total.count(produto)}")

#%% [markdown]
# # Exercício 10 - Identificar boletos vencidos

#%% [code]
data_atual = "2025-08-12"

boletos = [
    "2025-08-05",  # vencido
    "2025-08-12",  # vence hoje
    "2025-08-15",  # ainda válido
    "2025-08-01"   # vencido
]

total_vencidos = 0

for i, vencimento in enumerate(boletos, start=1):
    if vencimento < data_atual:
        situacao = "vencido"
        total_vencidos += 1
    elif vencimento == data_atual:
        situacao = "vence hoje"
    else:
        situacao = "dentro do prazo"
    
    print(f"Boleto: {i} | Vencimento: {vencimento} | Situação: {situacao}")

print("\nTotal de boletos vencidos:", total_vencidos)

#%% [markdown]
# # Exercício 11 - Decodificar mensagem cifrada

#%% [code]
# Mensagem encriptada
mensagem = "SbwKrQ eh phokRu q MDydvfulsW"

chave = mensagem.count("D") + mensagem.count("d") + mensagem.count("W")

mensagem_decodificada = ""

for c in mensagem:
    if c.isalpha() and len(c) > 0:
        if ord('A') <= ord(c) <= ord('Z'):
            novo = ord(c) - chave
            if novo < ord('A'):
                novo += 26
            mensagem_decodificada += chr(novo)
        elif ord('a') <= ord(c) <= ord('z'):
            novo = ord(c) - chave
            if novo < ord('a'):
                novo += 26
            mensagem_decodificada += chr(novo)
        else:
            mensagem_decodificada += c
    else:
        mensagem_decodificada += c

print("Mensagem decodificada:", mensagem_decodificada)

#%% [markdown]
# # Exercício 12 -  Otimizar verificação de sensores

#%% [code]
temperaturas = [28, 31, 27, 35, 29]

for i in range(len(temperaturas)):
    if temperaturas[i] > 30:
        print(f"Sensor {i+1} acima do limite")

