package org.example.Questao07;
import java.util.Scanner;

public class Questao07 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Nome do aluno: ");
        String nome = scanner.nextLine();

        System.out.print("Matricula: ");
        String matricula = scanner.nextLine();

        System.out.print("Nota 1: ");
        double nota1 = scanner.nextDouble();

        System.out.print("Nota 2: ");
        double nota2 = scanner.nextDouble();

        System.out.print("Nota 3: ");
        double nota3 = scanner.nextDouble();

        Aluno aluno = new Aluno(nome, matricula, nota1, nota2, nota3);
        aluno.verificarAprovacao();
        scanner.close();
    }
}
