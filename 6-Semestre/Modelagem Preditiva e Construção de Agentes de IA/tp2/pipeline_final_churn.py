"""
Pipeline final de classificação de churn (NeoStream).

Decisões de design
------------------
1. Split estratificado (stratify=y): o churn é ~18% da base; sem estratificar,
   treino e teste poderiam ter proporções diferentes e a métrica ficaria instável.
2. Split ANTES de qualquer fit: scaler/encoder só podem aprender com o treino,
   senão o teste vaza informação para o modelo (data leakage).
3. ColumnTransformer: as features são heterogêneas (numéricas e categóricas) e
   cada tipo exige um transformador; um único objeto organiza tudo e descarta
   colunas que não são features (cliente_id, ltv_alto).
4. OneHotEncoder(handle_unknown="ignore"): categorias inéditas em produção não
   quebram a previsão.
5. Pipeline em vez de passos manuais: pré-processamento e modelo viram um único
   objeto, treinado e aplicado do mesmo jeito em treino, validação e produção.
6. GridSearchCV sobre o Pipeline (parâmetro classificador__C): o pré-processamento
   é re-ajustado dentro de cada fold, então a validação cruzada também não vaza.
7. Métrica roc_auc: com ~18% de churn, acurácia seria enganosa.
8. Pipeline final salvo com joblib: o artefato único é o que vai para o deploy.
"""
import joblib
import pandas as pd
from sklearn.base import clone
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

ARQUIVO = "assinantes_neostream.csv"
ARQUIVO_MODELO = "pipeline_churn.joblib"
ALVO = "churn"
COLUNAS_NUMERICAS = ["tempo_assinatura_meses", "uso_medio_semanal_horas", "numero_reclamacoes"]
COLUNAS_CATEGORICAS = ["plano", "metodo_pagamento", "dispositivo_principal"]
GRADE_C = {"classificador__C": [0.01, 0.1, 1, 10, 100]}


def dividir_dados(caminho=ARQUIVO):
    df = pd.read_csv(caminho)
    X, y = df.drop(columns=[ALVO]), df[ALVO]
    return train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


def construir_pipeline():
    preprocessador = ColumnTransformer([
        ("numericas", StandardScaler(), COLUNAS_NUMERICAS),
        ("categoricas", OneHotEncoder(handle_unknown="ignore"), COLUNAS_CATEGORICAS),
    ])
    return Pipeline([
        ("preprocessador", preprocessador),
        ("classificador", LogisticRegression(max_iter=1000)),
    ])


def buscar_hiperparametros(pipeline, X_train, y_train):
    busca = GridSearchCV(pipeline, GRADE_C, cv=5, scoring="roc_auc", n_jobs=-1)
    return busca.fit(X_train, y_train)


def treinar_pipeline_final(pipeline, melhores_parametros, X_train, y_train):
    return clone(pipeline).set_params(**melhores_parametros).fit(X_train, y_train)


def avaliar(pipeline, X_test, y_test):
    previsoes = pipeline.predict(X_test)
    print(f"ROC AUC no teste: {roc_auc_score(y_test, pipeline.predict_proba(X_test)[:, 1]):.4f}")
    print(classification_report(y_test, previsoes, digits=3))


def main():
    X_train, X_test, y_train, y_test = dividir_dados()

    pipeline = construir_pipeline()
    busca = buscar_hiperparametros(pipeline, X_train, y_train)
    print("Melhores parâmetros:", busca.best_params_)
    print(f"ROC AUC (cv=5): {busca.best_score_:.4f}")

    pipeline_final = treinar_pipeline_final(pipeline, busca.best_params_, X_train, y_train)
    avaliar(pipeline_final, X_test, y_test)

    joblib.dump(pipeline_final, ARQUIVO_MODELO)
    print(f"Pipeline salvo em {ARQUIVO_MODELO}")


if __name__ == "__main__":
    main()
