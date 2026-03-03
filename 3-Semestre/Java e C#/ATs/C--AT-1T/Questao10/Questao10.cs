using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao10
{
    internal class Questao10
    {
        public static void Executar()
        {
            Random random = new Random();
            int numeroSecreto = random.Next(1, 51);
            int tentativas = 5;

            Console.WriteLine("Bem-vindo ao Jogo de Adivinhação!");
            Console.WriteLine("Tente adivinhar o número entre 1 e 50.");

            for (int tentativa = 1; tentativa <= tentativas; tentativa++)
            {
                Console.Write($"Tentativa {tentativa}/{tentativas}: ");
                string input = Console.ReadLine();
                int palpite;

                if (!int.TryParse(input, out palpite))
                {
                    Console.WriteLine("Erro! Digite um número válido.");
                    continue;
                }

                if (palpite < 1 || palpite > 50)
                {
                    Console.WriteLine("Erro! O número deve estar entre 1 e 50.");
                    continue;
                }

                if (palpite == numeroSecreto)
                {
                    Console.WriteLine($"Parabéns! Você acertou o número {numeroSecreto}.");
                    return;
                }
                else if (palpite < numeroSecreto) {
                    Console.WriteLine("O número é maior!");
                }
                else{Console.WriteLine("O número é menor!");}
            }

            Console.WriteLine($"Fim de jogo! O número era {numeroSecreto}.");
        }
    }
}

