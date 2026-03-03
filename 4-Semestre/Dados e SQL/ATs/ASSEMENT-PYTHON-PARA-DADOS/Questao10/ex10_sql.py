import pandas as pd
from sqlalchemy import create_engine

csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""
# Tentativa de carregar CSV diretamente da string (inválido)
df = pd.read_csv(csv_dados)

print("Arquivo carregado!")

# Tentativa de acessar coluna que pode não existir
media_valor = df["valor"].mean()
print("Média calculada:", media_valor)

# Manipulação de coluna inexistente
media_categoria = df["origem"].value_counts()
print("Contagem:", media_categoria)

# Criar conexão com banco SQL (em arquivo)
engine = create_engine("sqlite:///meubanco.db")

conn = engine.connect()

# Tentativa de escrever tabela sem verificar df
df.to_sql("tabela_dados", conn, if_exists="replace", index=False)
print("Tabela gravada com sucesso!")

# Tentativa de consulta sem validação
consulta = conn.execute("SELECT * FROM tabela_dados;")
for linha in consulta:
    print(linha)

conn.close()

print("Pipeline executado com sucesso!")
