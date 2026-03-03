import pandas as pd
from sqlalchemy import create_engine

try:
    engine = create_engine("sqlite:///:memory:")

    df = pd.read_csv("dados_scraping.csv")

    print("CSV carregado com sucesso!")
    print(df.head(), "\n")

    df.to_sql("tabela_scraping", engine, index=False, if_exists="replace")
    print("Tabela 'tabela_scraping' criada no banco.\n")

    consulta = pd.read_sql_query("SELECT * FROM tabela_scraping;", engine)

    print("Resultado da consulta SQL:")
    print(consulta)

except Exception as e:
    print("Erro no exercício 9:", e)
