package org.example.TP2;

import java.util.Scanner;

public class Questao7 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o seu salário bruto anual: R$ ");
        double salarioBrutoAnual = scanner.nextDouble();

        double imposto = 0;
        double salarioLiquido = salarioBrutoAnual;

        if (salarioBrutoAnual <= 22847.76) {
            imposto = 0;
        } else if (salarioBrutoAnual <= 33919.80) {
            imposto = salarioBrutoAnual * 0.075;
        } else if (salarioBrutoAnual <= 45012.60) {
            imposto = salarioBrutoAnual * 0.15;
        } else if (salarioBrutoAnual <= 55976.16) {
            imposto = salarioBrutoAnual * 0.225;
        } else {
            imposto = salarioBrutoAnual * 0.275;
        }

        salarioLiquido = salarioBrutoAnual - imposto;

        System.out.printf("Imposto de renda a pagar: R$ %.2f%n", imposto);
        System.out.printf("Salário líquido: R$ %.2f%n", salarioLiquido);

        scanner.close();
    }
}
