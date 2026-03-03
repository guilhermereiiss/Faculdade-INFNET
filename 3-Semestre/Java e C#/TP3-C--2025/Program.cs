using TP3_C__2025.AreaVolume;
using TP3_C__2025.MatriculaFaculdade;
using TP3_C__2025.TP3;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("\nEscolha a questão para executar:");
            Console.WriteLine("1 - Conceitos de Classe, Objeto, Campos e Métodos (C#)");
            Console.WriteLine("2 - (Exercícios 2 a 6): Venda de Show");
            Console.WriteLine("3 - (Exercícios 7 a 9): Matrícula Faculdade");
            Console.WriteLine("4- (Exercícios 10 a 12: Áreas e Volumes em C#");
            Console.WriteLine("0 - Sair");
            Console.Write("Opção: ");

            string opcao = Console.ReadLine();
            Console.Clear();

            switch (opcao)
            {
                case "1":
                    Questao01.Executar();
                    break;
                case "2":
                    Ingresso.Executar();
                    break;
                case "3":
                    Matricula.Executar();
                    break;
                case "4":
                    CalculoGeral.Executar();
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