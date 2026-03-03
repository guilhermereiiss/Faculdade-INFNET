using System;
using System.Globalization;

namespace TP2_C__2025.TP2
{
    internal class Questao6()
    {
        public static void Executar()
        {
            Console.Write("Digite seu peso em (kg):");
            double peso = Convert.ToDouble(Console.ReadLine());

            Console.Write("Digite sua altura em (m):");
            double altura = Convert.ToDouble(Console.ReadLine(), new CultureInfo("en-US"));

            double imc = peso / (altura * altura);


            if (imc < 18.5)
            {
                Console.WriteLine("Abaixo do peso");
            }
            else if (imc < 25)
            {
                Console.WriteLine("Peso normal");
            }
            else if (imc < 30)
            {
                Console.WriteLine("Sobrepeso");
            }
            else if (imc < 35)
            {
                Console.WriteLine("Obesidade grau 1");
            }
            else if (imc < 40)
            {
                Console.WriteLine("Obesidade grau 2");
            }
            else
            {
                Console.WriteLine("Obesidade grau 3");
            }
        }
    }
}