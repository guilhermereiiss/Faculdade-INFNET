
using System;

namespace TP2_C__2025.TP2
{
    internal class Questao2
    {
        public static void Executar()
        {
            Console.Write("Digite sua data de nascimento (dd/MM/yyyy): ");
            if (DateTime.TryParseExact(Console.ReadLine(), "dd/MM/yyyy", null, System.Globalization.DateTimeStyles.None, out DateTime dataNascimento))
            {
                DateTime hoje = DateTime.Today;
                DateTime proximoAniversario = new DateTime(hoje.Year, dataNascimento.Month, dataNascimento.Day);

                if (proximoAniversario < hoje)
                {
                    proximoAniversario = proximoAniversario.AddYears(1);
                }

                int diasFaltando = (proximoAniversario - hoje).Days;
                Console.WriteLine($"Faltam {diasFaltando} dias para o seu próximo aniversário!");
            }
            else
            {
                Console.WriteLine("Data inválida. Tente novamente.");
            }
        }
    }
}
