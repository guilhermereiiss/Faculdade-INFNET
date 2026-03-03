using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace AgenciaViagem.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Clientes",
                columns: table => new
                {
                    ClienteId = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    NomeCompleto = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    EnderecoEmail = table.Column<string>(type: "TEXT", nullable: false),
                    NumeroTelefone = table.Column<string>(type: "TEXT", nullable: false),
                    DataCadastro = table.Column<DateTime>(type: "TEXT", nullable: false),
                    StatusAtivo = table.Column<bool>(type: "INTEGER", nullable: false),
                    DataExclusao = table.Column<DateTime>(type: "TEXT", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Clientes", x => x.ClienteId);
                });

            migrationBuilder.CreateTable(
                name: "PacotesTuristicos",
                columns: table => new
                {
                    PacoteTuristicoId = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    TituloPacote = table.Column<string>(type: "TEXT", maxLength: 200, nullable: false),
                    DescricaoCompleta = table.Column<string>(type: "TEXT", nullable: false),
                    DataPartida = table.Column<DateTime>(type: "TEXT", nullable: false),
                    DataRetorno = table.Column<DateTime>(type: "TEXT", nullable: false),
                    CapacidadeMaximaViajantes = table.Column<int>(type: "INTEGER", nullable: false),
                    ValorPorPessoa = table.Column<decimal>(type: "decimal(10,2)", nullable: false),
                    NumeroDiarias = table.Column<int>(type: "INTEGER", nullable: false),
                    StatusAtivo = table.Column<bool>(type: "INTEGER", nullable: false),
                    DataExclusao = table.Column<DateTime>(type: "TEXT", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_PacotesTuristicos", x => x.PacoteTuristicoId);
                });

            migrationBuilder.CreateTable(
                name: "PaisesDestinos",
                columns: table => new
                {
                    PaisDestinoId = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    NomePais = table.Column<string>(type: "TEXT", maxLength: 50, nullable: false),
                    CodigoPais = table.Column<string>(type: "TEXT", maxLength: 5, nullable: false),
                    ContinenteLocalizacao = table.Column<string>(type: "TEXT", nullable: false),
                    StatusAtivo = table.Column<bool>(type: "INTEGER", nullable: false),
                    DataExclusao = table.Column<DateTime>(type: "TEXT", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_PaisesDestinos", x => x.PaisDestinoId);
                });

            migrationBuilder.CreateTable(
                name: "Reservas",
                columns: table => new
                {
                    ReservaId = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    ClienteId = table.Column<int>(type: "INTEGER", nullable: false),
                    PacoteTuristicoId = table.Column<int>(type: "INTEGER", nullable: false),
                    DataHoraReserva = table.Column<DateTime>(type: "TEXT", nullable: false),
                    NumeroPassageiros = table.Column<int>(type: "INTEGER", nullable: false),
                    ValorTotalReserva = table.Column<decimal>(type: "decimal(10,2)", nullable: false),
                    DescontoAplicado = table.Column<decimal>(type: "decimal(10,2)", nullable: false),
                    StatusReserva = table.Column<string>(type: "TEXT", nullable: false),
                    ObservacoesAdicionais = table.Column<string>(type: "TEXT", nullable: false),
                    DataCancelamento = table.Column<DateTime>(type: "TEXT", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Reservas", x => x.ReservaId);
                    table.ForeignKey(
                        name: "FK_Reservas_Clientes_ClienteId",
                        column: x => x.ClienteId,
                        principalTable: "Clientes",
                        principalColumn: "ClienteId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_Reservas_PacotesTuristicos_PacoteTuristicoId",
                        column: x => x.PacoteTuristicoId,
                        principalTable: "PacotesTuristicos",
                        principalColumn: "PacoteTuristicoId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "CidadesDestinos",
                columns: table => new
                {
                    CidadeDestinoId = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    NomeCidade = table.Column<string>(type: "TEXT", maxLength: 100, nullable: false),
                    DescricaoTuristica = table.Column<string>(type: "TEXT", nullable: false),
                    PaisDestinoId = table.Column<int>(type: "INTEGER", nullable: false),
                    StatusAtivo = table.Column<bool>(type: "INTEGER", nullable: false),
                    DataExclusao = table.Column<DateTime>(type: "TEXT", nullable: true)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_CidadesDestinos", x => x.CidadeDestinoId);
                    table.ForeignKey(
                        name: "FK_CidadesDestinos_PaisesDestinos_PaisDestinoId",
                        column: x => x.PaisDestinoId,
                        principalTable: "PaisesDestinos",
                        principalColumn: "PaisDestinoId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateTable(
                name: "CidadeDestinoPacoteTuristico",
                columns: table => new
                {
                    DestinosIncluidosCidadeDestinoId = table.Column<int>(type: "INTEGER", nullable: false),
                    PacotesIncluidosPacoteTuristicoId = table.Column<int>(type: "INTEGER", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_CidadeDestinoPacoteTuristico", x => new { x.DestinosIncluidosCidadeDestinoId, x.PacotesIncluidosPacoteTuristicoId });
                    table.ForeignKey(
                        name: "FK_CidadeDestinoPacoteTuristico_CidadesDestinos_DestinosIncluidosCidadeDestinoId",
                        column: x => x.DestinosIncluidosCidadeDestinoId,
                        principalTable: "CidadesDestinos",
                        principalColumn: "CidadeDestinoId",
                        onDelete: ReferentialAction.Cascade);
                    table.ForeignKey(
                        name: "FK_CidadeDestinoPacoteTuristico_PacotesTuristicos_PacotesIncluidosPacoteTuristicoId",
                        column: x => x.PacotesIncluidosPacoteTuristicoId,
                        principalTable: "PacotesTuristicos",
                        principalColumn: "PacoteTuristicoId",
                        onDelete: ReferentialAction.Cascade);
                });

            migrationBuilder.CreateIndex(
                name: "IX_CidadeDestinoPacoteTuristico_PacotesIncluidosPacoteTuristicoId",
                table: "CidadeDestinoPacoteTuristico",
                column: "PacotesIncluidosPacoteTuristicoId");

            migrationBuilder.CreateIndex(
                name: "IX_CidadesDestinos_PaisDestinoId",
                table: "CidadesDestinos",
                column: "PaisDestinoId");

            migrationBuilder.CreateIndex(
                name: "IX_Reservas_ClienteId",
                table: "Reservas",
                column: "ClienteId");

            migrationBuilder.CreateIndex(
                name: "IX_Reservas_PacoteTuristicoId",
                table: "Reservas",
                column: "PacoteTuristicoId");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "CidadeDestinoPacoteTuristico");

            migrationBuilder.DropTable(
                name: "Reservas");

            migrationBuilder.DropTable(
                name: "CidadesDestinos");

            migrationBuilder.DropTable(
                name: "Clientes");

            migrationBuilder.DropTable(
                name: "PacotesTuristicos");

            migrationBuilder.DropTable(
                name: "PaisesDestinos");
        }
    }
}
