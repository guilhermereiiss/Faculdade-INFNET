hora = "21:10"
hora_minutos = hora.split(":")
print("Horas:", hora_minutos[0])
print("Minutos:", hora_minutos[1])

# Converte um valor total de minutos em horas e minutos

total_minutos = 150
horas = total_minutos // 60      # divisão inteira
minutos = total_minutos % 60     # resto da divisão

print("Horas:", horas)
print("Minutos:", minutos)
print("Formato final:", f"{horas:02d}:{minutos:02d}")


# Soma duas horas e mostra o total em minutos

hora1 = "02:30"
hora2 = "01:45"

h1, m1 = map(int, hora1.split(":"))
h2, m2 = map(int, hora2.split(":"))

total_min1 = h1 * 60 + m1
total_min2 = h2 * 60 + m2

soma_minutos = total_min1 + total_min2

horas_finais = soma_minutos // 60
minutos_finais = soma_minutos % 60

print("Soma total:", f"{horas_finais:02d}:{minutos_finais:02d}")


# Converte segundos em formato "HH:MM:SS"

total_segundos = 3672

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos)
print("Formato final:", f"{horas:02d}:{minutos:02d}:{segundos:02d}")


# Calcula quantos minutos há entre duas horas

hora_inicio = "08:15"
hora_fim = "11:00"

h1, m1 = map(int, hora_inicio.split(":"))
h2, m2 = map(int, hora_fim.split(":"))

minutos_inicio = h1 * 60 + m1
minutos_fim = h2 * 60 + m2

diferenca = minutos_fim - minutos_inicio

print("Diferença em minutos:", diferenca)
