package org.example.Questao09;

public class Questao09 {
    public static void main(String[] args) {
        ContaBancaria minhaConta = new ContaBancaria("Guilherme Reis", 0);

        minhaConta.depositar(1000);
        minhaConta.exibirSaldo();

        minhaConta.sacar(500);
        minhaConta.exibirSaldo();

        minhaConta.sacar(600); 
        minhaConta.exibirSaldo();
    }
}
