import pandas as pd

try:
    df = pd.read_json("dados_scraping.json").T

    df = df.rename(columns={
        "Jogo": "nome_jogo",
        "Jogadores": "qtd_jogadores",
        "Lancamento": "ano_lancamento" 
    })

    df_filtrado = df[df["ano_lancamento"].astype(int) > 2015]

    df_filtrado.to_excel("relatorio_final.xlsx", index=False)

    print("Arquivo relatorio_final.xlsx salvo com sucesso!")

except Exception as e:
    print("Erro ao gerar relatório Excel:", e)
