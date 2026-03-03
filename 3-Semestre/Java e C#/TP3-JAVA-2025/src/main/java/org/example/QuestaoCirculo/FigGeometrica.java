package org.example.QuestaoCirculo;

public class FigGeometrica {
    public static void main(String[] args) {
        Circulo circulo = new Circulo(3.0);
        System.out.println("Área do Círculo: " + circulo.calcularArea());

        Esfera esfera = new Esfera(5.0);
        System.out.println("Volume da Esfera: " + esfera.calcularVolume());
    }
}
