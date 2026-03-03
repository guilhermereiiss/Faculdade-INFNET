package org.example.TP2;

import java.time.LocalDate;
import java.util.Scanner;

public class Questao4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite o dia de nascimento: ");
        int diaNascimento = scanner.nextInt();

        System.out.print("Digite o mês de nascimento: ");
        int mesNascimento = scanner.nextInt();

        System.out.print("Digite o ano de nascimento: ");
        int anoNascimento = scanner.nextInt();

        int diasVividos = calcularDiasVividos(diaNascimento, mesNascimento, anoNascimento);

        System.out.println("Você tem " + diasVividos + " dias de vida.");

        scanner.close();
    }

    public static int calcularDiasVividos(int dia, int mes, int ano) {
        int dias = 0;

        LocalDate dataAtual = LocalDate.now();

        int anoAtual = dataAtual.getYear();
        int mesAtual = dataAtual.getMonthValue();
        int diaAtual = dataAtual.getDayOfMonth();

        LocalDate dataNascimento = LocalDate.of(ano, mes, dia);
        LocalDate dataAtualDate = LocalDate.of(anoAtual, mesAtual, diaAtual);

        dias = (int) java.time.temporal.ChronoUnit.DAYS.between(dataNascimento, dataAtualDate);

        return dias;
    }
}
