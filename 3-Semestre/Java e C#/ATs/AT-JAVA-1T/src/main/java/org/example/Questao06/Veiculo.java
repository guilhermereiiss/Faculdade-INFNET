package org.example.Questao06;

public class Veiculo {
    private String placa;
    private String modelo;
    private int anoFabricacao;
    private double quilometragem;

    public Veiculo(String placa, String modelo, int anoFabricacao, double quilometragem) {
        this.placa = placa;
        this.modelo = modelo;
        this.anoFabricacao = anoFabricacao;
        this.quilometragem = quilometragem;
    }

    public void exibirDetalhes() {
        System.out.println("Placa: " + placa);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano de Fabricação: " + anoFabricacao);
        System.out.println("Quilometragem: " + quilometragem + " km");
        System.out.println();
        System.out.println();
    }

    public void registrarViagem(double km) {
        if (km > 0) {
            this.quilometragem += km;
            System.out.println("Viagem registrada! Nova quilometragem: " + this.quilometragem + " km");
        } else {
            System.out.println("Distancia invalida para registrar viagem.");
        }
    }
}

