using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao12
{
    internal class Contato
    {
        public string Nome { get; set; }
        public string Telefone { get; set; }
        public string Email { get; set; }

        public Contato(string nome, string telefone, string email)
        {
            Nome = nome;
            Telefone = telefone;
            Email = email;
        }
    }

    abstract class ContatoFormatter
    {
        public abstract void ExibirContatos(List<Contato> contatos);
    }

    class MarkdownFormatter : ContatoFormatter
    {
        public override void ExibirContatos(List<Contato> contatos)
        {
            Console.WriteLine("## Lista de Contatos\n");
            foreach (var contato in contatos)
            {
                Console.WriteLine($"- Nome: {contato.Nome}\n");
                Console.WriteLine($"-  Telefone: {contato.Telefone}\n");
                Console.WriteLine($"-  Email: {contato.Email}\n");
            }
        }
    }

    class TabelaFormatter : ContatoFormatter
    {
        public override void ExibirContatos(List<Contato> contatos)
        {
            Console.WriteLine("----------------------------------------");
            Console.WriteLine("| Nome          | Telefone       | Email            |");
            Console.WriteLine("----------------------------------------");
            foreach (var contato in contatos)
            {
                Console.WriteLine($"| {contato.Nome,-12} | {contato.Telefone,-13} | {contato.Email,-15} |");
            }
            Console.WriteLine("----------------------------------------");
        }
    }

    class RawTextFormatter : ContatoFormatter
    {
        public override void ExibirContatos(List<Contato> contatos)
        {
            foreach (var contato in contatos)
            {
                Console.WriteLine($"Nome: {contato.Nome} | Telefone: {contato.Telefone} | Email: {contato.Email}");
            }
        }
    }
}

