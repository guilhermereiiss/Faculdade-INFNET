package org.example.QuestaoCirculo;

public class Circulo {
    private double raio;

    public Circulo(double raio) {
        this.raio = raio;
    }

    public double calcularArea() {
        return Math.PI * (raio * raio);
    }

}

