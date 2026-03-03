// See https://aka.ms/new-console-template for more information


class Program
{
    static void Main()
    {
        Console.WriteLine("Qual é o seu nome?");
        string nome = Console.ReadLine();
        Console.WriteLine($"Olá, {nome}!");

      
        Variaveis();
        TesteSimples();
    }

    static void Variaveis()
    {
        int idade = 18;
        string nome = "Guilherme";
        double altura = 1.75;

        Console.WriteLine("Nome: " + nome);
        Console.WriteLine("Idade: " + idade);
        Console.WriteLine("Altura: " + altura);

        Console.ReadLine();
    }

    static void TesteSimples()
    {
        string nome = "Marcos";  
        int idade = 25;        

        Console.WriteLine($"Meu nome é {nome} e eu tenho {idade} anos.");
    }
}


