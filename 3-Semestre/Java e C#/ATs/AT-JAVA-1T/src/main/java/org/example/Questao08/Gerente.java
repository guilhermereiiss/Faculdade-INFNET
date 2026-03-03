package org.example.Questao08;

public class Gerente extends Funcionario {
    public Gerente(String nome, double salario) {
        super(nome, salario);
    }

    @Override
    public double calcularSalario() {
        return salario*1.2;
    }
}
