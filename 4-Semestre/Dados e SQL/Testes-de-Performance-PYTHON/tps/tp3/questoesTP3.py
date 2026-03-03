from  questao01 import  main01
from  questao02 import  main02
from questao03 import  main03
from questao04 import  main04
from questao05 import  main05
from questao06 import  main06
from questao07 import main07
from questao08 import main08
from questao09 import main09
from questao12 import main12


exercicios = {
    "1": main01 ,
    "2": main02 ,
    "3": main03 ,
    "4": main04,
    "5": main05 ,
    "6":  main06,
    "7": main07,
    "8": main08,
    "9": main09,
    # "10": main,
    # "11": main,
    "12": main12,
}

print("Lista de Exercicios do TP3 de Python - GUILHERME REIS")
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

