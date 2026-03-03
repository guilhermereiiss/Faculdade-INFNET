using Microsoft.EntityFrameworkCore;
using AgenciaViagem.Models;

public class AgenciaViagemContext : DbContext
{
    public DbSet<Cliente> Clientes { get; set; }
    public DbSet<CidadeDestino> CidadesDestinos { get; set; }
    public DbSet<PaisDestino> PaisesDestinos { get; set; }
    public DbSet<PacoteTuristico> PacotesTuristicos { get; set; }
    public DbSet<Reserva> Reservas { get; set; }

    public AgenciaViagemContext(DbContextOptions<AgenciaViagemContext> options)
        : base(options)
    {
    }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
    {
        if (!optionsBuilder.IsConfigured)
        {
            optionsBuilder.UseSqlite("Data Source=agencia_viagem.db");
        }
    }
}