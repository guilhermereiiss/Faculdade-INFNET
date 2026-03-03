using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP2_C__2025.TP2
{
    internal class Questao7
    {
        public static void Executar()
        {
            Console.Write("Digite um número inteiro: ");
            int numero = int.Parse(Console.ReadLine());
            if (numero % 2 == 0)
            {
                Console.WriteLine("O número é par.");
            }
            else
            {
                Console.WriteLine("O número é ímpar.");
            }
        }
    }
}
