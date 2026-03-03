using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao03
{
    internal class Questao03
    {
        public static void Executar()
        {
            double numero1, numero2, resultado;
            int opcao;

            Console.Write("Digite o primeiro número: ");
            while (!double.TryParse(Console.ReadLine(), out numero1))
            {
                Console.Write("Entrada inválida! Por favor, insira um número válido: ");
            }

            Console.Write("Digite o segundo número: ");
            while (!double.TryParse(Console.ReadLine(), out numero2))
            {
                Console.Write("Entrada inválida! Por favor, insira um número válido: ");
            }

            Console.WriteLine("\nEscolha a operação desejada:");
            Console.WriteLine("1 - Soma");
            Console.WriteLine("2 - Subtração");
            Console.WriteLine("3 - Multiplicação");
            Console.WriteLine("4 - Divisão");

            while (!int.TryParse(Console.ReadLine(), out opcao) || opcao < 1 || opcao > 4)
            {
                Console.Write("Opção inválida! Escolha uma operação válida (1-4): ");
            }

            switch (opcao)
            {
                case 1:
                    resultado = numero1 + numero2;
                    Console.WriteLine($"\nResultado da soma: {resultado}");
                    break;
                case 2:
                    resultado = numero1 - numero2;
                    Console.WriteLine($"\nResultado da subtração: {resultado}");
                    break;
                case 3:
                    resultado = numero1 * numero2;
                    Console.WriteLine($"\nResultado da multiplicação: {resultado}");
                    break;
                case 4:
                    if (numero2 == 0){
                        Console.WriteLine("\nErro: Divisão por zero não é permitida.");
                    }
                    else{
                        resultado = numero1 / numero2;
                        Console.WriteLine($"\nResultado da divisão: {resultado}");
                    }
                    break;
            }
        }
    }
}
