using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP2_C__2025.TP2
{
    internal class Questao10
    {
        public static void Executar()
        {
            Console.Write("Digite um número: ");
            int numero = int.Parse(Console.ReadLine());

            
            for (int i = numero; i >= 0; i--)
            {

                Console.Write(i);

                if (i > 0)
                {
                    Console.Write(", ");
                }
            }

            Console.WriteLine();
        }
    }
}
