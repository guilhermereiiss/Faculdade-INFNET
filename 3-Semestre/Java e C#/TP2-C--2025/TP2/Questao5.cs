using System;
using System.Globalization;

namespace TP2_C__2025.TP2
{
    internal class Questao5()
    {
        static (double, double) ConverterTemperatura(double celsius)
        {
            double fahrenheit = celsius * 9 / 5 + 32;
            double kelvin = celsius + 273.15;
            return (fahrenheit, kelvin);
        }

        public static void Executar()
        {
            Console.Write("Digite a temperatura em graus Celsius: ");
            double celsius = double.Parse(Console.ReadLine());

            var (fahrenheit, kelvin) = ConverterTemperatura(celsius);

            Console.WriteLine($"A temperatura em Fahrenheit é: {fahrenheit:F2}°F");
            Console.WriteLine($"A temperatura em Kelvin é: {kelvin:F2}K");
        }
    }
}