package org.example.QuestaoCirculo;

public class Esfera {
    private double raiO;

    public Esfera(double raiO) {
        this.raiO = raiO;
    }

    public double calcularVolume() {
        return (4.0 / 3.0) * Math.PI * (raiO * raiO * raiO);
    }

}