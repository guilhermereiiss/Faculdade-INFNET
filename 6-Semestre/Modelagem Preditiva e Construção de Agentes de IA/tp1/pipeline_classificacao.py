from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline

from preparo_dados import carregar_dados, dividir_treino_teste, separar_alvo
from preprocessamento_heterogeneo import construir_preprocessador


def construir_pipeline():
    return Pipeline([
        ("preprocessador", construir_preprocessador()),
        ("classificador", LogisticRegression(max_iter=1000)),
    ])


def main():
    X, y = separar_alvo(carregar_dados())
    X_train, X_test, y_train, y_test = dividir_treino_teste(X, y)

    pipeline = construir_pipeline()
    pipeline.fit(X_train, y_train)
    previsoes = pipeline.predict(X_test)

    print("Previsões geradas:", previsoes.shape[0])
    print(f"Proporção prevista de churn: {previsoes.mean():.2%}")
    print(classification_report(y_test, previsoes, digits=3))


if __name__ == "__main__":
    main()
