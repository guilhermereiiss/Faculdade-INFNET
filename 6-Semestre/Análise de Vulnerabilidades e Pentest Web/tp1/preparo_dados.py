import pandas as pd
from sklearn.model_selection import train_test_split

ARQUIVO = "assinantes_neostream.csv"
ALVO = "churn"
COLUNAS_NUMERICAS = ["tempo_assinatura_meses", "uso_medio_semanal_horas", "numero_reclamacoes"]
COLUNAS_CATEGORICAS = ["plano", "metodo_pagamento", "dispositivo_principal"]


def carregar_dados(caminho=ARQUIVO):
    return pd.read_csv(caminho)


def separar_alvo(df):
    return df.drop(columns=[ALVO]), df[ALVO]


def dividir_treino_teste(X, y):
    return train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
