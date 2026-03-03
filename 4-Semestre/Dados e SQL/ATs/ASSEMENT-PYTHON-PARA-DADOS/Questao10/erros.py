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

# ERRO 1 — FileNotFoundError
# pd.read_csv NÃO pode receber o conteúdo bruto da string,
# ele espera um caminho de arquivo OU um buffer.
df = pd.read_csv(csv_dados)

print("Arquivo carregado!")

# ERRO 2 — KeyError
# A coluna "valor" existe, mas se o erro anterior ocorrer,
# df nunca será criado → causa UnboundLocalError antes mesmo daqui.
media_valor = df["valor"].mean()
print("Média calculada:", media_valor)

# ERRO 3 — KeyError
# A coluna "origem" NÃO existe no CSV → KeyError imediato.
media_categoria = df["origem"].value_counts()
print("Contagem:", media_categoria)

# Criar conexão com banco SQL (em arquivo)
engine = create_engine("sqlite:///meubanco.db")

# POSSÍVEL ERRO — Caso engine falhe, aqui daria OperationalError
conn = engine.connect()

# ERRO 4 — DataFrame inválido
# Se df não existir por causa dos erros acima → UnboundLocalError
df.to_sql("tabela_dados", conn, if_exists="replace", index=False)
print("Tabela gravada com sucesso!")

# ERRO 5 — Se a tabela não foi criada por falha no to_sql
# → DatabaseError / sqlalchemy.exc.OperationalError
consulta = conn.execute("SELECT * FROM tabela_dados;")
for linha in consulta:
    print(linha)

conn.close()

print("Pipeline executado com sucesso!")
