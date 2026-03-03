package org.example.QuestaoProduto;

public class Produto {

    // Questões de 2 a 6.

    private String nome;
    private double preco;
    private int quantidadeEmEstoque;

    public Produto(String nome, double preco, int quantidadeEmEstoque) {
        this.nome = nome;
        this.preco = preco;
        this.quantidadeEmEstoque = quantidadeEmEstoque;
    }

    // Get e Set
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public int getQuantidadeEmEstoque() {
        return quantidadeEmEstoque;
    }

    public void setQuantidadeEmEstoque(int quantidadeEmEstoque) {
        this.quantidadeEmEstoque = quantidadeEmEstoque;
    }

    public void alterarPreco(double novoPreco) {
        this.preco = novoPreco;
    }

    public void alterarQuantidade(int novaQuantidade) {
        this.quantidadeEmEstoque = novaQuantidade;
    }

    public void exibirInformacoes() {
        System.out.println("Nome: " + nome);
        System.out.println("Preço: R$ " + preco);
        System.out.println("Quantidade em Estoque: " + quantidadeEmEstoque);
    }

    public static void main(String[] args) {
        Produto produto = new Produto("Arroz", 5.99, 20);

        System.out.println("Informações Iniciais do Produto:");
        produto.exibirInformacoes();

        produto.alterarPreco(6.49);
        produto.alterarQuantidade(25);

        System.out.println("\nInformações Atualizadas do Produto:");
        produto.exibirInformacoes();

        produto.setNome("Feijão");
        produto.setPreco(7.99);
        produto.setQuantidadeEmEstoque(30);

        System.out.println("\nInformações após uso dos Setters:");
        System.out.println("Nome: " + produto.getNome());
        System.out.println("Preço: R$ " + produto.getPreco());
        System.out.println("Quantidade em Estoque: " + produto.getQuantidadeEmEstoque());
    }


}
