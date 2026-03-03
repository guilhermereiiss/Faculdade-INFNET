using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AT_C_.Questao07
{
    internal class ContaBancaria
    {
        public string Titular { get; private set; }
        private decimal saldo;

        public ContaBancaria(string titular)
        {
            Titular = titular;
            saldo = 0;
        }

        public void Depositar(decimal valor)
        {
            if (valor > 0)
            {
                saldo += valor;
                Console.WriteLine($"Depósito de R$ {valor:F2} realizado com sucesso.");
            }
            else
            {
                Console.WriteLine("O valor do depósito deve ser positivo!");
            }
        }

        public void Sacar(decimal valor)
        {
            if (valor > saldo)
            {
                Console.WriteLine("Saldo insuficiente para realizar o saque!");
            }
            else
            {
                saldo -= valor;
                Console.WriteLine($"Saque de R$ {valor:F2} realizado com sucesso!");
            }
        }

       public void ExibirSaldo(){Console.WriteLine($"Saldo atual: R$ {saldo:F2}");
        }
    

        public static void Executar()
        {
            ContaBancaria conta = new ContaBancaria("Rinaldo Sampaio");
            Console.WriteLine($"Titular: {conta.Titular}\n");

            conta.Depositar(500);
            conta.ExibirSaldo();

            Console.WriteLine("\nTentativa de saque: R$ 700,00");
            conta.Sacar(700);

            conta.Sacar(200);
            conta.ExibirSaldo();
        }
    }
}
