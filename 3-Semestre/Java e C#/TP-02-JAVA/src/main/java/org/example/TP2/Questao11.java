package org.example.TP2;

import java.util.Scanner;

public class Questao11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o valor inicial: ");
        int valorInicial = scanner.nextInt();

        System.out.print("Digite o incremento: ");
        int incremento = scanner.nextInt();

        System.out.println("Sequencia abaixo:");

        for (int i = valorInicial; i <= 100; i += incremento) {
            System.out.print(i);
            if (i + incremento <= 100) {
                System.out.print(", ");
            }
        }

        scanner.close();
    }
}
