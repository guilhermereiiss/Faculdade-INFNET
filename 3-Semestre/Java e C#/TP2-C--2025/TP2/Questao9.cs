using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP2_C__2025.TP2
{
    internal class Questao9
    {
        public static void Executar()
        {
            Console.Write("Digite o salário bruto: R$ ");
            double salarioBruto = Convert.ToDouble(Console.ReadLine(), new CultureInfo("en-US"));

            
            double descontoImposto = 0;

            if (salarioBruto <= 2000)
            {
                descontoImposto = salarioBruto * 0.05;
            }
            else if (salarioBruto <= 5000)
            {
                descontoImposto = salarioBruto * 0.1;
            }
            else
            {
                descontoImposto = salarioBruto * 0.15; 
            }

            double salarioLiquido = salarioBruto - descontoImposto;

            Console.WriteLine("\n=== Resultados ===");
            Console.WriteLine($"Salário Bruto: R$ {salarioBruto:F2}");
            Console.WriteLine($"Desconto de Imposto: R$ {descontoImposto:F2}");
            Console.WriteLine($"Salário Líquido: R$ {salarioLiquido:F2}");
        }
    }
}

