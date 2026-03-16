from pathlib import Path

def listar_diretorio(caminho, nivel=0):
    print("  " * nivel + caminho.name)

    for item in caminho.iterdir():
        if item.is_dir():
            listar_diretorio(item, nivel + 1)
        else:
            print("  " * (nivel + 1) + item.name)

listar_diretorio(Path("."))