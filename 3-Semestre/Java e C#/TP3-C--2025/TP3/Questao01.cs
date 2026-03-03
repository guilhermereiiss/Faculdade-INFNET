using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TP3_C__2025.TP3
{
    internal class Questao01
    {
        // Classe representa um modelo ou estrutura que define atributos e comportamentos de um objeto.
        // No exemplo abaixo, a classe "Carro" representa um carro com suas características e funções.
        class Carro
        {
            // Campos (ou atributos) são variáveis que armazenam os dados do objeto.
            public string Modelo;
            public int Ano;

            // Método é uma função dentro da classe que define um comportamento.
            // Aqui, o método ExibirDetalhes mostra as informações do carro.
            public void ExibirDetalhes()
            {
                Console.WriteLine($"Modelo: {Modelo}, Ano: {Ano}");
            }
        }

        public static void Executar()
        {

            // Criamos um objeto da classe Carro
            Carro meuCarro = new Carro();

            // Atribuímos valores aos campos do objeto
            meuCarro.Modelo = "Toyota Corolla";
            meuCarro.Ano = 2020;

            // Chamamos o método do objeto, que exibe os detalhes do carro
            meuCarro.ExibirDetalhes();
        
        }
    }
}
