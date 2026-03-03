using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace AT_C_.Questao11
{
    internal class Questao11
    {
        static string caminhoArquivo = "C:\\Users\\guilh\\source\\repos\\AT-C#\\Questao11\\contato.txt";
        public static void Executar()
        {
            int opcao;

            do
            {
                ExibirMenu();
                opcao = ObterOpcaoUsuario();

                switch (opcao)
                {
                    case 1:
                        AdicionarContato();
                        break;
                    case 2:
                        ListarContatos();
                        break;
                    case 3:
                        Console.WriteLine("Encerrando programa...");
                        break;
                    default:
                        Console.WriteLine("Opção inválida. Tente novamente.");
                        break;
                }
            } while (opcao != 3);
        }

        static void ExibirMenu()
        {
            Console.Clear();
            Console.WriteLine("=== Gerenciador de Contatos ===");
            Console.WriteLine("1 - Adicionar novo contato");
            Console.WriteLine("2 - Listar contatos cadastrados");
            Console.WriteLine("3 - Sair");
            Console.Write("Escolha uma opção: ");
        }

        static int ObterOpcaoUsuario()
        {
            int opcao;
            while (!int.TryParse(Console.ReadLine(), out opcao) || opcao < 1 || opcao > 3)
            {
                Console.Write("Opção inválida. Escolha uma opção entre 1 e 3: ");
            }
            return opcao;
        }

        static void AdicionarContato()
        {
            Console.Clear();
            Console.WriteLine("=== Adicionar Novo Contato ===");

            Console.Write("Nome: ");
            string nome = Console.ReadLine();

            Console.Write("Telefone: ");
            string telefone = Console.ReadLine();

            Console.Write("Email: ");
            string email = Console.ReadLine();
            string contato = $"{nome},{telefone},{email}";

            try
            {
                using (StreamWriter sw = new StreamWriter(caminhoArquivo, true))
                {
                    sw.WriteLine(contato);
                }
                Console.WriteLine("Contato cadastrado com sucesso!");
            }
            catch (Exception ex) { Console.WriteLine($"Erro ao salvar o contato: {ex.Message}"); }

            Console.WriteLine("Pressione qualquer tecla para voltar ao menu.");
            Console.ReadKey();
        }

        static void ListarContatos()
        {
            Console.Clear();
            Console.WriteLine("=== Listar Contatos Cadastrados ===");

            if (File.Exists(caminhoArquivo))
            {
                string[] contatos = File.ReadAllLines(caminhoArquivo);

                if (contatos.Length > 0)
                {
                    Console.WriteLine("Contatos cadastrados:");
                    foreach (var contato in contatos)
                    {
                        string[] partes = contato.Split(',');
                        Console.WriteLine($"Nome: {partes[0]} | Telefone: {partes[1]} | Email: {partes[2]}");
                    }
                }
                else { Console.WriteLine("Nenhum contato cadastrado."); }
            }
            else
            {
                Console.WriteLine("Nenhum contato cadastrado.");
                Console.WriteLine("Pressione qualquer tecla para voltar ao menu.");
                Console.ReadKey();
            }
        }
    }
}
