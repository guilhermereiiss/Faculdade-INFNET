using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP2_C__2025.TP2
{
    internal class Questao8
    {
        public static void Executar()
        {
            Console.Write("Digite a nota (0 a 10): ");
            double nota = Convert.ToDouble(Console.ReadLine(), new CultureInfo("en-US"));

            if (nota >= 0 && nota <= 3)
            {
                Console.WriteLine("Classificação: Insuficiente");
            }
            else if (nota > 3 && nota <= 6)
            {
                Console.WriteLine("Classificação: Regular");
            }
            else if (nota > 6 && nota <= 9)
            {
                Console.WriteLine("Classificação: Bom");
            }
            else if (nota == 10)
            {
                Console.WriteLine("Classificação: Excelente");
            }
            else
            { 
                Console.WriteLine("Nota inválida! A nota deve estar entre 0 e 10.");
            }
        }
    }
}
