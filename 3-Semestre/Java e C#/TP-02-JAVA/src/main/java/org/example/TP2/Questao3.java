package org.example.TP2;

import java.util.Scanner;

public class Questao3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor em reais: ");
        double valorReais = scanner.nextDouble();

        System.out.print("Escolha a moeda de destino (dólar, euro ou libra): ");
        String moedaDestino = scanner.next().toLowerCase();

        double taxaCambio = 0;

        if (moedaDestino.equals("dólar")) {
            taxaCambio = 5.83;
        } else if (moedaDestino.equals("euro")) {
            taxaCambio = 6.06;
        } else if (moedaDestino.equals("libra")) {
            taxaCambio = 7.35;
        } else {
            System.out.println("Moeda não reconhecida.");
            scanner.close();
            return;
        }

        double valorConvertido = valorReais / taxaCambio;

        System.out.printf("Valor convertido: %.2f %s\n", valorConvertido, moedaDestino);

        scanner.close();
    }
}
