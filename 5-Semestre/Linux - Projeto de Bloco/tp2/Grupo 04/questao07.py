def calcular_tamanho(pasta):
    total = 0

    for item in pasta.values():
        if isinstance(item, dict):
            total += calcular_tamanho(item)
        else:
            total += item

    return total

sistema_arquivos = {
  "Documentos": {
    "Trabalho": {"projeto1.pdf": 500, "projeto2.pdf": 300},
    "Pessoal": {"receitas.txt": 10},
  },
  "Imagens": {
    "Ferias": {"foto1.jpg": 2000, "foto2.jpg": 3000},
    "logo.png": 150
  },
  "README.txt": 5
}

total = calcular_tamanho(sistema_arquivos)
print("Tamanho total:", total)