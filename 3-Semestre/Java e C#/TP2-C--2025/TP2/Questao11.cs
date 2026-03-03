using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP2_C__2025.TP2
{
    internal class Questao11
    {
        public static void Executar()
        {
            Console.Write("Digite um número para ver a tabuada: ");
            int numero = int.Parse(Console.ReadLine());

            for (int i = 1; i <= 10; i++)
            {
                int resultado = numero * i;
                Console.WriteLine($"{numero} x {i} = {resultado}");
            }
        }
    }
}
