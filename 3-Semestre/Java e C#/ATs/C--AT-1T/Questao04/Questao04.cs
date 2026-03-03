using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao04
{
    internal class Questao04
    {
        public static void Executar()
        {
            Console.Write("Digite sua data de nascimento (dd/MM/yyyy): ");
            if (DateTime.TryParseExact(Console.ReadLine(), "dd/MM/yyyy", null, DateTimeStyles.None, out DateTime dataNascimento))
            {
                DateTime hoje = DateTime.Today;
                DateTime proximoAniversario = new DateTime(hoje.Year, dataNascimento.Month, dataNascimento.Day);

                if (proximoAniversario < hoje)
                {
                    proximoAniversario = proximoAniversario.AddYears(1);
                }

                int diasFaltando = (proximoAniversario - hoje).Days;
                Console.WriteLine($"Faltam {diasFaltando} dias para o seu próximo aniversário.");

                if (diasFaltando < 7)
                {
                    Console.WriteLine("Está chegando! Prepare-se para comemorar seu aniversario!");
                }
            }
            else
            {
                Console.WriteLine("Data inválida. Tente novamente.");
            }
        }
    }
}
