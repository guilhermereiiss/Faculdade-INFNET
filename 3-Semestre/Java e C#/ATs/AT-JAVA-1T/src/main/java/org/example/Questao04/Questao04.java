package org.example.Questao04;
import java.util.Scanner;

public class Questao04 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite o valor do emprestimo: ");
        double valorEmprestimo = scanner.nextDouble();

        System.out.print("Em quantas parcelas deseja pagar? (minimo é 6 e maximo é 48): ");
        int parcelas = scanner.nextInt();

        if (parcelas < 6 || parcelas > 48) {
            System.out.println("Numero de parcelas invalido! Deve estar entre 6 e 48.");
            return;
        }
        double taxaJuros = 0.03;
        double valorTotalPago = valorEmprestimo * Math.pow(1 + taxaJuros, parcelas);
        double valorParcela = valorTotalPago / parcelas;

        System.out.println("\nSimulação de Emprestimo para " + nome + ": ");
        System.out.printf("- Valor Total Pago: R$ %.2f\n", valorTotalPago);
        System.out.printf("- Valor da Parcela: R$ %.2f (%dx)\n", valorParcela, parcelas);
        scanner.close();
    }
}
