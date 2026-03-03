using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao02
{
    internal class Questao02
    {
        static string CifrarNome(string nome)
        {
            char[] nomeArray = nome.ToCharArray();

            for (int i = 0; i < nomeArray.Length; i++)
            {
                if (Char.IsLetter(nomeArray[i]))
                {
                    char movido = nomeArray[i];

                    if (Char.IsUpper(movido))
                    {
                        movido = (char)((movido - 'A' + 2) % 26 + 'A');
                    }
                    else if (Char.IsLower(movido))
                    {
                        movido = (char)((movido - 'a' + 2) % 26 + 'a');
                    }
                    nomeArray[i] = movido;
                }
            }
            return new string(nomeArray);
        }

        public static void Executar()
        {
            Console.WriteLine("Digite seu nome completo ( Ex:Carlos Silva ):");
            string nome = Console.ReadLine();
            string nomeCifrado = CifrarNome(nome);

            Console.WriteLine($"Nome cifrado: {nomeCifrado}");
        }
    }
}
