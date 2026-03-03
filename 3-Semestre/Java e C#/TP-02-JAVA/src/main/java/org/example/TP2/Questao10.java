package org.example.TP2;

import java.util.Random;
import java.util.Scanner;

public class Questao10 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int numeroSecreto = random.nextInt(100) + 1;

        int palpite = 0;
        int tentativas = 0;

        System.out.println("Bem-vindo ao Jogo de Adivinhação!");
        System.out.println("Eu pensei em um número entre 1 e 100. Tente adivinhar!");

        while (palpite != numeroSecreto) {
            System.out.print("Digite seu palpite: ");
            palpite = scanner.nextInt();
            tentativas++;

            if (palpite < numeroSecreto) {
                System.out.println("Seu palpite é menor do que o número secreto.");
            } else if (palpite > numeroSecreto) {
                System.out.println("Seu palpite é maior do que o número secreto.");
            } else {
                System.out.println("Parabéns! Você acertou o número secreto!");
                System.out.println("Número de tentativas: " + tentativas);
            }
        }

        scanner.close();
    }
}
