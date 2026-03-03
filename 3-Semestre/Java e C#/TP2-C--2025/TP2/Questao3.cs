using System;

namespace TP2_C__2025.TP2
{
    internal class Questao3
    {
       
        public static void Executar()
        {
            Console.WriteLine("Digite a primeira data (dd/MM/yyyy):");
            DateTime data1 = DateTime.ParseExact(Console.ReadLine(), "dd/MM/yyyy", null);

            Console.WriteLine("Digite a segunda data (dd/MM/yyyy):");
            DateTime data2 = DateTime.ParseExact(Console.ReadLine(), "dd/MM/yyyy", null);

            
            if (data1 > data2)
            {
                var temp = data1;
                data1 = data2;
                data2 = temp;
            }

            TimeSpan diferenca = data2 - data1;

            int anos = data2.Year - data1.Year;
            int meses = data2.Month - data1.Month;
            int dias = data2.Day - data1.Day;

            if (dias < 0)
            {
                meses--;
                dias += DateTime.DaysInMonth(data1.Year, data1.Month);
            }

            if (meses < 0)
            {
                anos--;
                meses += 12;
            }

            Console.WriteLine($"Diferença: {anos} anos, {meses} meses e {dias} dias.");
        }
    }
}
