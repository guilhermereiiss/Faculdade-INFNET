using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao08
{
    internal class Funcionario
    {
            public string Nome { get; private set; }
            public string Cargo { get; private set; }
            public decimal SalarioBase { get; private set; }

            public Funcionario(string nome, string cargo, decimal salarioBase)
            {
                Nome = nome;
                Cargo = cargo;
                SalarioBase = salarioBase;
            }

            public virtual decimal CalcularSalario(){return SalarioBase;}

            public void ExibirSalario()
            {
                Console.WriteLine($"{Nome} ({Cargo}) - Salário: R$ {CalcularSalario():F2}");
            }
        

        class Gerente : Funcionario
        {
            public Gerente(string nome, decimal salarioBase) : base(nome, "Gerente", salarioBase) { }
            public override decimal CalcularSalario(){ return SalarioBase * 1.2m;}
        }
        public static void Executar()
        {
           Funcionario funcionario = new Funcionario("Carlos Silva", "Analista", 3000);
           Gerente gerente = new Gerente("Mariana Souza", 5000);

           funcionario.ExibirSalario();
           gerente.ExibirSalario();
        }
        
    }
}
