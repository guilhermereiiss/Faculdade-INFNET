package org.example.TP2;

import java.util.Scanner;

public class Questao1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome completo: ");
        String nomeCompleto = scanner.nextLine();

        System.out.print("Digite sua idade: ");
        int idade = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Digite o nome da sua mãe: ");
        String nomeMae = scanner.nextLine();

        System.out.print("Digite o nome do seu pai: ");
        String nomePai = scanner.nextLine();

        System.out.println("\n=== Informações Cadastradas ===");
        System.out.println("Nome completo: " + nomeCompleto);
        System.out.println("Idade: " + idade + " anos");
        System.out.println("Nome da mãe: " + nomeMae);
        System.out.println("Nome do pai: " + nomePai);

        int tamanhoNomeCompleto = nomeCompleto.length();
        int tamanhoNomeMae = nomeMae.length();
        int tamanhoNomePai = nomePai.length();

        if (tamanhoNomeCompleto > tamanhoNomeMae && tamanhoNomeCompleto > tamanhoNomePai) {
            System.out.println("\nSeu nome completo tem mais letras do que o nome da sua mãe e do seu pai.");
        } else if (tamanhoNomeMae > tamanhoNomeCompleto && tamanhoNomeMae > tamanhoNomePai) {
            System.out.println("\nO nome da sua mãe tem mais letras do que o seu nome e o nome do seu pai.");
        } else if (tamanhoNomePai > tamanhoNomeCompleto && tamanhoNomePai > tamanhoNomeMae) {
            System.out.println("\nO nome do seu pai tem mais letras do que o seu nome e o nome da sua mãe.");
        } else {
            System.out.println("\nPelo menos dois nomes possuem o mesmo número de letras.");
        }

        scanner.close();
    }
}
