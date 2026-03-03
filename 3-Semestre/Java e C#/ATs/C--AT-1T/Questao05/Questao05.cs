using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao05
{
    internal class Questao05
    {
        public static void Executar()
        {
            {
                DateTime dataFormatura = new DateTime(2027, 12, 15);

                Console.Write("Digite a data atual (dd/MM/yyyy): ");
                string entradaData = Console.ReadLine();

                if (DateTime.TryParseExact(entradaData, "dd/MM/yyyy", null, System.Globalization.DateTimeStyles.None, out DateTime dataAtual))
                {
                    if (dataAtual > DateTime.Now)
                    {
                        Console.WriteLine("Erro: A data informada não pode ser no futuro!");
                    }
                    else
                    {
                        TimeSpan diferenca = dataFormatura - dataAtual;

                        if (dataAtual > dataFormatura)
                        {
                            Console.WriteLine("Parabéns! Você já dever estar formado!");
                        }
                        else
                        {
                            int anos = (dataFormatura.Year - dataAtual.Year);
                            int meses = dataFormatura.Month - dataAtual.Month;
                            int dias = dataFormatura.Day - dataAtual.Day;

                            if (meses < 0)
                            {
                                anos--;
                                meses += 12;
                            }

                            if (dias < 0)
                            {
                                meses--;
                                dias += DateTime.DaysInMonth(dataAtual.Year, dataAtual.Month);
                            }

                            Console.WriteLine($"Faltam {anos} anos, {meses} meses e {dias} dias para sua formatura!");
                            if (anos == 0 && meses < 6)
                            {
                                Console.WriteLine("A reta final chegou! Prepare-se para a formatura!");
                            }
                        }
                    }
                }
                else
                {
                    Console.WriteLine("Erro: A data informada é inválida!");
                }
            }
        }
    }
}
