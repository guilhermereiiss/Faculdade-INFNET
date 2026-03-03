using System;
using static TP2_C__2025.TP2.Questao3;

namespace TP2_C__2025.TP2
{
    internal class Questao4
    {
        public static void Executar()
        {
            Console.Write("Digite seu nome: ");
            string nome = Console.ReadLine();

            Console.Write("Digite sua idade: ");
            int idade = int.Parse(Console.ReadLine());

            Console.Write("Digite seu telefone: ");
            string telefone = Console.ReadLine();

            Console.Write("Digite seu e-mail: ");
            string email = Console.ReadLine();

            Console.WriteLine("\nCadastro Realizado com Sucesso!\n");
            Console.WriteLine("Dados Cadastrados:");
            Console.WriteLine($"Nome: {nome}");
            Console.WriteLine($"Idade: {idade} anos");
            Console.WriteLine($"Telefone: {telefone}");
            Console.WriteLine($"E-mail: {email}");
        }
    }
}
