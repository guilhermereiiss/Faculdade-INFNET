package org.example.QuestaoBancaria;

public class TestaConta {
    public static void main(String[] args) {
        Conta conta = new Conta("João Silva", 12345, "001", 1000.0, "10/03/2025");

        System.out.println("Informações iniciais da conta:");
        conta.exibirInformacoes();

        System.out.println("\nSacando R$ 200...");
        boolean saqueRealizado = conta.saca(200);
        System.out.println("Saque realizado: " + saqueRealizado);
        conta.exibirInformacoes();

        System.out.println("\nDepositando R$ 500...");
        conta.deposita(500);
        conta.exibirInformacoes();

        double rendimento = conta.calculaRendimento();
        System.out.println("\nRendimento mensal esperado: R$ " + rendimento);
    }
}
