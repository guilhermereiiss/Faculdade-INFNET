
using AT_C_.Questao01;
using AT_C_.Questao02;
using AT_C_.Questao03;
using AT_C_.Questao04;
using AT_C_.Questao05;
using AT_C_.Questao06;
using AT_C_.Questao07;
using AT_C_.Questao08;
using AT_C_.Questao09;
using AT_C_.Questao10;
using AT_C_.Questao11;
using AT_C_.Questao12;

class Program
{
    static void Main()
    {
        while (true)
        {
            Console.WriteLine("\nEscolha a questão para executar:");
            Console.WriteLine("1 - Criando e Executando seu Primeiro Programa");
            Console.WriteLine("2 - Manipulação de Strings - Cifrador de Nome");
            Console.WriteLine("3 - Calculadora de Operações Matemáticas");
            Console.WriteLine("4 - Manipulação de Datas - Dias até o Próximo Aniversário");
            Console.WriteLine("5 - Tempo Restante para Conclusão do Curso - Diferença Entre Datas");
            Console.WriteLine("6 - Cadastro de Alunos");
            Console.WriteLine("7 - Banco Digital (Encapsulamento)");
            Console.WriteLine("8 - Cadastro de Funcionários (Herança)");
            Console.WriteLine("9 - Controle de Estoque via Linha de Comando");
            Console.WriteLine("10 - Jogo de Adivinhação");
            Console.WriteLine("11 - Manipulação de Arquivos - Cadastro e Listagem de Contatos");
            Console.WriteLine("12 - Manipulação de Arquivos com Herança e Polimorfismo - Formatos de Exibição");
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
                    Questao02.Executar();
                    break;
                case "3":
                    Questao03.Executar();
                    break;
                case "4":
                    Questao04.Executar();
                    break;
                case "5":
                    Questao05.Executar();
                    break;
                case "6":
                    Aluno.Executar();
                    break;
                case "7":
                    ContaBancaria.Executar();
                    break;
                case "8":
                    Funcionario.Executar();
                    break;
                case "9":
                    Questao09.Executar();
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