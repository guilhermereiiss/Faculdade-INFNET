import pandas as pd

try:
    df = pd.read_json("dados_scraping.json").T

    print("Colunas encontradas:", df.columns)

    df = df.rename(columns={
        "Jogo": "nome_jogo",
        "Jogadores": "qtd_jogadores",
        "Lancamento": "ano_lancamento"   
    })

    df_filtrado = df[df["ano_lancamento"].astype(int) > 2015]

    print("\nResultado filtrado:")
    print(df_filtrado)

except Exception as e:
    print("Erro ao processar JSON:", e)
