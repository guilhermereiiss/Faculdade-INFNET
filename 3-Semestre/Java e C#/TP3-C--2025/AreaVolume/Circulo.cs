using System;

public class Circulo
{
    public double Raio { get; set; }

    public Circulo(double raio)
    {
        Raio = raio;
    }

    public double CalcularArea()
    {
        return Math.PI * (Raio * Raio);
    }
}

public class Esfera
{
    public double Raio { get; set; }

    public Esfera(double raio)
    {
        Raio = raio;
    }
    public double CalcularVolume()
    {
        return (4.0 / 3.0) * Math.PI * (Raio * Raio * Raio);
    }
}
