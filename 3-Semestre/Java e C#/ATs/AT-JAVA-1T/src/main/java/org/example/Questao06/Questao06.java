package org.example.Questao06;

public class Questao06 {
    public static void main(String[] args) {
        Veiculo carro1 = new Veiculo("NEYMAR-1234", "Sedan", 2020, 50000);
        Veiculo carro2 = new Veiculo("JAVA-5678", "SUV", 2018, 75000);

        System.out.println("Dados iniciais dos veiculos:");
        carro1.exibirDetalhes();
        carro2.exibirDetalhes();

        System.out.println("Registrando viagens...");
        carro1.registrarViagem(120);
        carro2.registrarViagem(200);

        System.out.println("\nDados atualizados dos veiculos:");
        carro1.exibirDetalhes();
        carro2.exibirDetalhes();
    }
}


