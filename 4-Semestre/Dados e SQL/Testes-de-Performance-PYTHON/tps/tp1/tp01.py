from ex01.exercicio01 import executar_exercicio01
from ex02.exercicio02 import executar_exercicio02
from ex03.exercicio03 import executar_exercicio03
from ex04.exercicio04 import executar_exercicio04
from ex05.exercicio05 import executar_exercicio05
from ex06.exercicio06 import executar_exercicio06
from ex07.exercicio07 import executar_exercicio07
from ex08.exercicio08 import executar_exercicio08
from ex09.exercicio09 import executar_exercicio09
from ex10.exercicio10 import executar_exercicio10
from ex11.exercicio11 import executar_exercicio11
from ex12.exercicio12 import executar_exercicio12


exercicios = {
    "1": executar_exercicio01,
    "2": executar_exercicio02,
    "3": executar_exercicio03,
    "4": executar_exercicio04,
    "5": executar_exercicio05,
    "6": executar_exercicio06,
    "7": executar_exercicio07,
    "8": executar_exercicio08,
    "9": executar_exercicio09,
    "10": executar_exercicio10,
    "11": executar_exercicio11,
    "12": executar_exercicio12,
}

print("Lista de Exercicios do TP1 de Python - GUILHERME REIS")
print("Escolha de 1 a 12, ou 'sair'. \n")

while True:
    questao = input("Digite qual exercicio vc quer ver (1 a 12): ")

    if questao.lower() == "sair":
        break

    if questao in exercicios:
        print(f"\n Rodando Exercício {questao}:\n")
        exercicios[questao]() 
    else:
        print("Esse exercicio não existe! Tente de novo.\n")

