package org.example.Questao09;

public class ContaBancaria {
    String titular;
    private double saldo;
    public String getTitular() {return titular;}
    public double getSaldo() {return saldo;}

    public ContaBancaria(String titular, double saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    public void depositar(double valor){
        if(valor > 0){
            saldo += valor;
            System.out.println("Deposito de R$ " + valor + " realizado com sucesso!");
        }else{
            System.out.println("Valor de deposito inválido.");
        }
    }

    public void sacar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Saque de R$ " + valor + " realizado com sucesso.");
        } else {
            System.out.println("Saldo insuficiente ou valor invalido para saque.");
        }
    }

    public void exibirSaldo() {
        System.out.println("Saldo da conta de " + titular + ": R$ " + saldo);
    }
}

