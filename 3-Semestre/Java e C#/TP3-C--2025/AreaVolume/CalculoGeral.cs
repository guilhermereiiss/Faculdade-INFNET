using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP3_C__2025.AreaVolume
{
    internal class CalculoGeral
    {
        public static void Executar()
        {
            Circulo circulo = new Circulo(3.0); // Raio do círculo = 3.0
            Esfera esfera = new Esfera(5.0);    // Raio da esfera = 5.0

            double areaCirculo = circulo.CalcularArea();
            Console.WriteLine($"A área do círculo com raio {circulo.Raio} é: {areaCirculo}");

            double volumeEsfera = esfera.CalcularVolume();
            Console.WriteLine($"O volume da esfera com raio {esfera.Raio} é: {volumeEsfera}");
        }
    }
}
