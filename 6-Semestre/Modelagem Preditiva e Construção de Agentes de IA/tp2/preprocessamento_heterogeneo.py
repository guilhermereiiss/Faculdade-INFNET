from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from preparo_dados import (
    COLUNAS_CATEGORICAS,
    COLUNAS_NUMERICAS,
    carregar_dados,
    dividir_treino_teste,
    separar_alvo,
)


def construir_preprocessador():
    return ColumnTransformer([
        ("numericas", StandardScaler(), COLUNAS_NUMERICAS),
        ("categoricas", OneHotEncoder(handle_unknown="ignore"), COLUNAS_CATEGORICAS),
    ])


def main():
    X, y = separar_alvo(carregar_dados())
    X_train, X_test, _, _ = dividir_treino_teste(X, y)

    preprocessador = construir_preprocessador()
    X_train_transformado = preprocessador.fit_transform(X_train)
    X_test_transformado = preprocessador.transform(X_test)

    print("Shape de X_train transformado:", X_train_transformado.shape)
    print("Shape de X_test transformado:", X_test_transformado.shape)


if __name__ == "__main__":
    main()
