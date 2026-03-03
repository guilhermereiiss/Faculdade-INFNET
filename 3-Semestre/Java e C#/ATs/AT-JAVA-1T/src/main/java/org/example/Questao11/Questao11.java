package org.example.Questao11;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class Questao11 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        Set<Integer> numerosSorteados = new HashSet<>();
        Set<Integer> numerosUsuario = new HashSet<>();

        while (numerosSorteados.size() < 6) {
            numerosSorteados.add(random.nextInt(60) + 1);
        }

        System.out.println("Digite 6 numeros entre 1 e 60:");
        while (numerosUsuario.size() < 6) {
            int num = scanner.nextInt();
            if (num < 1 || num > 60) {
                System.out.println("Numero invalido, Digite um numero entre 1 e 60.");
            } else if (!numerosUsuario.add(num)) {
                System.out.println("Numero repetido, Digite um numero diferente.");
            }
        }

        Set<Integer> acertos = new HashSet<>(numerosUsuario);
        acertos.retainAll(numerosSorteados);

        System.out.println("\nNumeros sorteados: " + numerosSorteados);
        System.out.println("Seus numeros: " + numerosUsuario);
        System.out.println("Voce acertou " + acertos.size() + " numero(s): " + acertos);
        scanner.close();
    }
}
