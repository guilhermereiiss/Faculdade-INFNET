using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP2_C__2025.TP2
{
    internal class Questao12
    {
        public static void Executar()
        {
            Random random = new Random();

            int numeroSecreto = random.Next(1, 101);
            int palpite = 0;
            Console.WriteLine("Bem-vindo ao Jogo de Adivinhação!");
            Console.WriteLine("Tente adivinhar o número secreto entre 1 e 100.");

            while (palpite != numeroSecreto)
            {
                Console.Write("Digite seu palpite: ");
                palpite = int.Parse(Console.ReadLine());

                if (palpite < numeroSecreto)
                {
                    Console.WriteLine("O número secreto é maior. Tente novamente!");
                }
                else if (palpite > numeroSecreto)
                {
                    Console.WriteLine("O número secreto é menor. Tente novamente!");
                }
            }

            Console.WriteLine($"Parabéns! Você acertou o número secreto: {numeroSecreto}");
        }
    }
}
