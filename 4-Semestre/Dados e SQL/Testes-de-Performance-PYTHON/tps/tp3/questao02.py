def main02():
    codigo_sensor = "MON2023-RN456-P01"

    ano = codigo_sensor[3:7]

    segmento_intermediario = codigo_sensor[8:13]

    unidade = codigo_sensor[-2:]

    print("Ano:", ano)
    print("Segmento intermediário:", segmento_intermediario)
    print("Unidade:", unidade)
