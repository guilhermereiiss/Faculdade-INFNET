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

try:
    buffer = io.StringIO(csv_dados)
    df = pd.read_csv(buffer)
    print("✓ CSV carregado com sucesso!")
except Exception as e:
    print("✗ Falha ao carregar o CSV:", e)
    df = None

if df is not None:
    print("\nPrévia do DataFrame:")
    print(df.head())

try:
    media_valor = df["valor"].mean()
except KeyError:
    print("\n✗ A coluna 'valor' não existe. Média não calculada.")
else:
    print("\n✓ Média calculada da coluna 'valor':", media_valor)


try:
    contagem_origem = df["origem"].value_counts()
except KeyError:
    print("\n! Coluna 'origem' não encontrada — operação ignorada.")
else:
    print("\nContagem da coluna 'origem':")
    print(contagem_origem)

engine = None
conn = None

try:  

    try:
        engine = create_engine("sqlite:///meubanco.db")
        conn = engine.connect()
        print("\n✓ Conexão SQL estabelecida!")
    except Exception as e:
        print("\n✗ Erro ao conectar ao banco SQLite:", e)

    if df is not None and conn is not None:
        try:
            df.to_sql("tabela_dados", conn, if_exists="replace", index=False)
        except Exception as e:
            print("\n✗ Erro ao salvar DataFrame na tabela SQL:", e)
        else:
            print("\n✓ Tabela 'tabela_dados' gravada com sucesso!")

        try:
            consulta = pd.read_sql_query("SELECT * FROM tabela_dados;", conn)
        except Exception as e:
            print("\n✗ Erro ao executar consulta SQL:", e)
        else:
            print("\n✓ Consulta SQL executada com sucesso!")
            print(consulta)

finally:
    if conn is not None:
        conn.close()
        print("\nConexão SQL encerrada.")

print("\n Pipeline corrigido e executado com sucesso!")
