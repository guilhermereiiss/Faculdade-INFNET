using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao12
{
    internal class Questao12
    {
        static string arquivo = "C:\\Users\\guilh\\source\\repos\\AT-C#\\Questao12\\contato.txt";

        public static void Executar()
        {
            List<Contato> contatos = LerContatos();

            Console.WriteLine("Escolha o formato de exibição:");
            Console.WriteLine("1 - Markdown");
            Console.WriteLine("2 - Tabela");
            Console.WriteLine("3 - Texto Puro");

            string escolha = Console.ReadLine();
            ContatoFormatter formatter = escolha switch
            {
                "1" => new MarkdownFormatter(),
                "2" => new TabelaFormatter(),
                "3" => new RawTextFormatter(),
                _ => null
            };

            if (formatter != null)
            {
                formatter.ExibirContatos(contatos);
            }
            else{ Console.WriteLine( "Opção inválida!" );}
        }

        static List<Contato> LerContatos()
        {
            List<Contato> contatos = new List<Contato>();
            if (File.Exists(arquivo))
            {
                foreach (var linha in File.ReadAllLines(arquivo))
                {
                    var partes = linha.Split(';');
                    if (partes.Length == 3)
                    {
                        contatos.Add(new Contato(partes[0], partes[1], partes[2]));
                    }
                }
            }
            return contatos;
        }
    }
}
