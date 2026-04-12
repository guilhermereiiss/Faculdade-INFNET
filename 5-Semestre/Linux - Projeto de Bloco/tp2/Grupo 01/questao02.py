import asyncio
import random
import time

async def baixar_arquivo(nome_arquivo):
    print(f"Iniciando download: {nome_arquivo}")

    if nome_arquivo == "virus.exe":
        raise Exception(f"Arquivo malicioso detectado: {nome_arquivo}")

    tempo_download = random.randint(1, 5)
    await asyncio.sleep(tempo_download)

    print(f"Download concluido: {nome_arquivo}")
    return nome_arquivo


async def main():
    arquivos = [
        "download (10).jpg",
        "Roblox PFP.jpg",
        "tp.pdf",
        "virus.exe"
    ]

    inicio = time.time()

    tarefas = [baixar_arquivo(arq) for arq in arquivos]

    resultados = await asyncio.gather(*tarefas, return_exceptions=True)

    fim = time.time()

    print("\nRelatorio final:")

    arquivos_baixados = []
    for resultado in resultados:
        if isinstance(resultado, Exception):
            print(f"Erro: {resultado}")
        else:
            arquivos_baixados.append(resultado)

    print(f"\nArquivos baixados: {arquivos_baixados}")
    print(f"Tempo total: {fim - inicio:.2f} segundos")


if __name__ == "__main__":
    asyncio.run(main())