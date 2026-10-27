import os
import zipfile
import sys

NOME_ZIP_PADRAO = "guilherme_reis_DR2_AT.ZIP"

DIRETORIOS_IGNORADOS = {
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".git",
    ".idea",
    ".vscode",
}

ARQUIVOS_IGNORADOS = {
    ".env",
    "clinica.db",
    "eventos.db",
}

EXTENSOES_IGNORADAS = {
    ".pyc",
    ".pyo",
    ".db",
    ".sqlite",
    ".sqlite3",
}


def empacotar_projeto(nome_zip: str = NOME_ZIP_PADRAO):
    caminho_base = os.path.dirname(os.path.abspath(__file__))
    caminho_zip_saida = os.path.join(caminho_base, nome_zip)

    print(f"Compactando projeto em: {caminho_zip_saida}")
    total_arquivos = 0

    with zipfile.ZipFile(caminho_zip_saida, "w", zipfile.ZIP_DEFLATED) as zipf:
        for raiz, dirs, arquivos in os.walk(caminho_base):
            # Filtra diretórios ignorados
            dirs[:] = [d for d in dirs if d not in DIRETORIOS_IGNORADOS]

            for arquivo in arquivos:
                if (
                    arquivo == nome_zip
                    or arquivo.endswith(".zip")
                    or arquivo.endswith(".ZIP")
                    or arquivo in ARQUIVOS_IGNORADOS
                ):
                    continue

                _, ext = os.path.splitext(arquivo)
                if ext in EXTENSOES_IGNORADAS:
                    continue

                # Ignora banco local gerado se preferir, ou inclui
                caminho_completo = os.path.join(raiz, arquivo)
                caminho_relativo = os.path.relpath(caminho_completo, caminho_base)

                zipf.write(caminho_completo, caminho_relativo)
                total_arquivos += 1
                print(f"  + {caminho_relativo}")

    tamanho_mb = os.path.getsize(caminho_zip_saida) / (1024 * 1024)
    print(f"\nSucesso! Arquivo '{nome_zip}' gerado com {total_arquivos} arquivos ({tamanho_mb:.2f} MB).")


if __name__ == "__main__":
    nome = sys.argv[1] if len(sys.argv) > 1 else NOME_ZIP_PADRAO
    empacotar_projeto(nome)
