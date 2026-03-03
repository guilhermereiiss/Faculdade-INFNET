using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP3_C__2025.MatriculaFaculdade
{
    public class Matricula
    {
        public string NomeDoAluno { get; set; }
        public string Curso { get; set; }
        public int NumeroMatricula { get; set; }
        public string Situacao { get; set; }
        public string DataInicial { get; set; }

        public Matricula(string nomeDoAluno, string curso, int numeroMatricula, string situacao, string dataInicial)
        {
            NomeDoAluno = nomeDoAluno;
            Curso = curso;
            NumeroMatricula = numeroMatricula;
            Situacao = situacao;
            DataInicial = dataInicial;
        }

        public void Trancar()
        {
            Situacao = "Trancada";
            Console.WriteLine($"Matrícula de {NomeDoAluno} foi trancada.");
        }

        public void Reativar()
        {
            Situacao = "Ativa";
            Console.WriteLine($"Matrícula de {NomeDoAluno} foi reativada.");
        }

        public void ExibirInformacoes()
        {
            Console.WriteLine($"Nome do Aluno: {NomeDoAluno}");
            Console.WriteLine($"Curso: {Curso}");
            Console.WriteLine($"Número da Matrícula: {NumeroMatricula}");
            Console.WriteLine($"Situação: {Situacao}");
            Console.WriteLine($"Data Inicial: {DataInicial}");
        }

        public static void Executar()
        {
            Matricula matricula = new Matricula("João Silva", "Engenharia de Software", 12345, "Ativa", "01/02/2023");

            Console.WriteLine("Informações iniciais da matrícula:");
            matricula.ExibirInformacoes();

            Console.WriteLine("\n------ Trancando a matrícula ------\n");

            matricula.Trancar();

            matricula.ExibirInformacoes();

            Console.WriteLine("\n------ Reativando a matrícula ------\n");

            matricula.Reativar();

            matricula.ExibirInformacoes();
        }
    }
}
