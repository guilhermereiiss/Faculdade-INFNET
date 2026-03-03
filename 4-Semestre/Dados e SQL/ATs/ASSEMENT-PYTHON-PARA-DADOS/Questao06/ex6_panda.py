import pandas as pd

try:
    df = pd.read_csv("dados_scraping.csv", usecols=["Jogo", "Jogadores"])

    print("Primeiras linhas:")
    print(df.head())

    df_ordenado = df.sort_values(by="Jogo")

    print("\nDataFrame ordenado:")
    print(df_ordenado)

except Exception as e:
    print("Erro ao carregar ou processar CSV:", e)
