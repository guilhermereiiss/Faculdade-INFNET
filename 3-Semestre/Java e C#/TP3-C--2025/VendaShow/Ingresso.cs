using System;

class Ingresso
{
    private string nomeDoShow;
    private double preco;
    private int quantidadeDisponivel;

    public Ingresso(string nomeDoShow, double preco, int quantidadeDisponivel)
    {
        this.nomeDoShow = nomeDoShow;
        this.preco = preco;
        this.quantidadeDisponivel = quantidadeDisponivel;
    }

    public void AlterarPreco(double novoPreco)
    {
        this.preco = novoPreco;
    }

    public void AlterarQuantidade(int novaQuantidade)
    {
        this.quantidadeDisponivel = novaQuantidade;
    }

    public string GetNomeDoShow()
    {
        return nomeDoShow;
    }

    public double GetPreco()
    {
        return preco;
    }

    public int GetQuantidadeDisponivel()
    {
        return quantidadeDisponivel;
    }

    public void SetNomeDoShow(string novoNome)
    {
        this.nomeDoShow = novoNome;
    }

    public void SetPreco(double novoPreco)
    {
        this.preco = novoPreco;
    }

    public void SetQuantidadeDisponivel(int novaQtd)
    {
        this.quantidadeDisponivel = novaQtd;
    }

    public void ExibirInformacoes()
    {
        Console.WriteLine($"Show: {nomeDoShow}");
        Console.WriteLine($"Preço: R$ {preco:F2}");
        Console.WriteLine($"Quantidade disponível: {quantidadeDisponivel}");
        Console.WriteLine();
    }

    public static void Executar()
    {
        Ingresso ingresso1 = new Ingresso("Rock Festival", 150.00, 50);

        Console.WriteLine("Informações Iniciais:");
        ingresso1.ExibirInformacoes();

        ingresso1.AlterarPreco(180.00);
        ingresso1.AlterarQuantidade(40);

        Console.WriteLine("Após Alterações:");
        ingresso1.ExibirInformacoes();

        ingresso1.SetNomeDoShow("Pop Music Festival");
        ingresso1.SetPreco(200.00);
        ingresso1.SetQuantidadeDisponivel(30);

        Console.WriteLine("Após uso de Setters:");
        Console.WriteLine($"Nome do Show: {ingresso1.GetNomeDoShow()}");
        Console.WriteLine($"Preço: R$ {ingresso1.GetPreco():F2}");
        Console.WriteLine($"Quantidade disponível: {ingresso1.GetQuantidadeDisponivel()}");
    }
}





