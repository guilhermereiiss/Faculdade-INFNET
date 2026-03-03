package org.example.QuestaoBancaria;

public class Conta {
    private String titular;
    private int numero;
    private String agencia;
    private double saldo;
    private String dataAbertura;

    public Conta(String titular, int numero, String agencia, double saldo, String dataAbertura) {
        this.titular = titular;
        this.numero = numero;
        this.agencia = agencia;
        this.saldo = saldo;
        this.dataAbertura = dataAbertura;
    }

    public boolean saca(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            return true;
        }
        return false;
    }

    public void deposita(double valor) {
        if (valor > 0) {
            saldo += valor;
        }
    }

    public double calculaRendimento() {
        return saldo * 0.1;
    }

    public void exibirInformacoes() {
        System.out.println("Titular: " + titular);
        System.out.println("Número: " + numero);
        System.out.println("Agência: " + agencia);
        System.out.println("Saldo: R$ " + saldo);
        System.out.println("Data de Abertura: " + dataAbertura);
    }
}


