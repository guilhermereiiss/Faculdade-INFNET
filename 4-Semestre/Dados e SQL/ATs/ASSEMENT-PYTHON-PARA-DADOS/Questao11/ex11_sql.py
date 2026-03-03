import pandas as pd
from sqlalchemy import create_engine
import io

csv_dados = """id,valor,categoria,descricao
1,250,credito,Deposito realizado no app
2,-100,debito,Pagamento de boleto
3,480,credito,Recebimento TED
4,-50,debito,Compra online
5,1020,credito,Salario mensal
6,-200,debito,Supermercado
"""


# 1) LEITURA ROBUSTA DO CSV
try:
    buffer = io.StringIO(csv_dados)
    df = pd.read_csv(buffer)
    print("✓ CSV carregado com sucesso!")
except Exception as e:
    print("✗ Falha ao carregar o CSV:", e)
    df = None  # evita quebra futura

# Mostrar DataFrame caso tenha sido carregado
if df is not None:
    print("\nPrévia do DataFrame:")
    print(df.head())


# 2) CÁLCULO DA MÉDIA DA COLUNA "valor"
try:
    media_valor = df["valor"].mean()
except KeyError:
    print("\n✗ A coluna 'valor' não existe. Média não calculada.")
else:
    print("\n✓ Média calculada da coluna 'valor':", media_valor)



# 3) TRATAMENTO DA COLUNA INEXISTENTE "origem"
try:
    contagem_origem = df["origem"].value_counts()
except KeyError:
    print("\n! Coluna 'origem' não encontrada — operação ignorada.")
    pass
else:
    print("\nContagem da coluna 'origem':")
    print(contagem_origem)
