using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao09
{
    internal class Questao09
    {
        const string arquivoEstoque = "C:\\Users\\guilh\\source\\repos\\AT-C#\\Questao09\\estoque.txt";
        static List<string> produtos = new List<string>();

        public static void Executar()
        {
            CarregarProdutos();

            while (true)
            {
                Console.WriteLine("\nMenu:");
                Console.WriteLine("1. Inserir Produto");
                Console.WriteLine("2. Listar Produtos");
                Console.WriteLine("3. Sair");
                Console.Write("Escolha uma opção: ");

                string opcao = Console.ReadLine();
                switch (opcao)
                {
                    case "1": InserirProduto(); break;
                    case "2": ListarProdutos(); break;
                    case "3": return;
                    default: Console.WriteLine("Opção inválida!"); break;
                }
            }
        }

        static void CarregarProdutos()
        {
            if (File.Exists(arquivoEstoque))
            {
                produtos.AddRange(File.ReadAllLines(arquivoEstoque));
            }
        }

        static void InserirProduto()
        {
            if (produtos.Count >= 5)
            {
                Console.WriteLine("Limite de produtos atingido!");
                return;
            }

            Console.Write("Nome do Produto: ");
            string nome = Console.ReadLine();

            Console.Write("Quantidade em estoque: ");
            if (!int.TryParse(Console.ReadLine(), out int quantidade))
            {
                Console.WriteLine("Quantidade inválida!");
                return;
            }

            Console.Write("Preço unitário: ");
            if (!decimal.TryParse(Console.ReadLine(), out decimal preco))
            {
                Console.WriteLine("Preço inválido!");
                return;
            }

            string produto = $"{nome},{quantidade},{preco:F2}";
            produtos.Add(produto);
            File.AppendAllText(arquivoEstoque, produto + "\n");
            Console.WriteLine("Produto cadastrado com sucesso!");
        }

        static void ListarProdutos()
        {
            if (produtos.Count == 0)
            {
                Console.WriteLine("Nenhum produto cadastrado.");
                return;
            }

            Console.WriteLine("\nLista de Produtos:");
            foreach (var linha in produtos)
            {
                string[] dados = linha.Split(',');
                Console.WriteLine($"Produto: {dados[0]} | Quantidade: {dados[1]} | Preço: R$ {dados[2]}");
            }
        }
    }
}
