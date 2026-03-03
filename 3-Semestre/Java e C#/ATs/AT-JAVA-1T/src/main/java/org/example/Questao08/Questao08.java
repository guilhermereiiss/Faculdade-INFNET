package org.example.Questao08;

public class Questao08 {
    public static void main(String[] args) {
        Gerente gerente = new Gerente("Eduarda", 15000);
        Estagiario estagiario = new Estagiario("Marcos",100);

        System.out.println("Salario do Gerente: R$ " + gerente.calcularSalario());
        System.out.println("Salario do Estagiario: R$ " + estagiario.calcularSalario());
    }
}
