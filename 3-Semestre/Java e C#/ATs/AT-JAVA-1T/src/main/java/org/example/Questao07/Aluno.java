package org.example.Questao07;

public class Aluno {

    private String nome;
    private String matricula;
    private double nota1, nota2, nota3;

    public Aluno(String nome, String matricula, double nota1, double nota2, double nota3) {
        this.nome = nome;
        this.matricula = matricula;
        this.nota1 = nota1;
        this.nota2 = nota2;
        this.nota3 = nota3;
    }

    public double calcularMedia() {
        return (nota1 + nota2 + nota3) / 3;
    }

    public void verificarAprovacao() {
        double media = calcularMedia();
        System.out.println("Média: " + media);
        if (media >= 7) {
            System.out.println("Foi: Aprovado");
        } else {
            System.out.println("Foi: Reprovado");
        }
    }
}

