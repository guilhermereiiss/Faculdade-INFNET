package org.example.Questao1;


class Carro {
    // Campos (atributos)
    String marca;
    int velocidade;

    // Construtor
    Carro(String marca, int velocidade) {
        this.marca = marca;
        this.velocidade = velocidade;
    }

    // Método para acelerar o carro
    void acelerar(int incremento) {
        velocidade += incremento;
        System.out.println("O carro acelerou. Velocidade atual: " + velocidade + " km/h");
    }
}

    // Classe principal para testar a classe "Carro"
    public class Carros {
    public static void main(String[] args) {

        Carro meuCarro = new Carro("Toyota", 50);

        System.out.println("Marca: " + meuCarro.marca);
        System.out.println("Velocidade inicial: " + meuCarro.velocidade + " km/h");

        meuCarro.acelerar(20);
    }
}
