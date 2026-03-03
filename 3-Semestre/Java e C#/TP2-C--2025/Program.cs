

using System;
using TP2_C__2025.TP2;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("\nEscolha a questão para executar:");
            Console.WriteLine("1 - Calcular idade exata");
            Console.WriteLine("2 - Dias para o próximo aniversário");
            Console.WriteLine("3 - Diferença entre duas datas");
            Console.WriteLine("4 - Formulário de Cadastro Simples");
            Console.WriteLine("5 - Conversor de Temperatura");
            Console.WriteLine("6 - Cálculo de IMC");
            Console.WriteLine("7 - Verificador de Número Par ou Ímpar");
            Console.WriteLine("8 - Classificação de Nota Escolar");
            Console.WriteLine("9 - Calculadora de Salário Líquido");
            Console.WriteLine("10 - Contagem Regressiva");
            Console.WriteLine("11 - Tabuada Interativa");
            Console.WriteLine("12 -  Jogo de Adivinhação");
            Console.WriteLine("0 - Sair");
            Console.Write("Opção: ");

            string opcao = Console.ReadLine();
            Console.Clear();

            switch (opcao)
            {
                case "1":
                    Questao1.Executar();
                    break;
                case "2":
                    Questao2.Executar();
                    break;
                case "3":
                    Questao3.Executar();
                    break;
                case "4":
                    Questao4.Executar();
                    break;
                case "5":
                    Questao5.Executar();
                    break;
                case "6":
                    Questao6.Executar();
                    break;
                case "7":
                    Questao7.Executar();
                    break;
                case "8":
                    Questao8.Executar();
                    break;
                case "9":
                    Questao9.Executar();
                    break;
                case "10":
                    Questao10.Executar();
                    break;
                case "11":
                    Questao11.Executar();
                    break;
                case "12":
                    Questao12.Executar();
                    break;
                case "0":
                    Console.WriteLine("Encerrando o programa...");
                    return;
                default:
                    Console.WriteLine("Opção inválida. Tente novamente.");
                    break;
            }
        }
    }
}
