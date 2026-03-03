using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AgenciaViagem.Models
{
    public class Reserva
    {
        public int ReservaId { get; set; }
        
        [Required]
        public int ClienteId { get; set; }
        public Cliente? ClienteReservante { get; set; }
        
        [Required]
        public int PacoteTuristicoId { get; set; }
        public PacoteTuristico? PacoteEscolhido { get; set; }
        
        public DateTime DataHoraReserva { get; set; }
        
        [Required(ErrorMessage = "Número de passageiros é obrigatório")]
        [Range(1, 10, ErrorMessage = "Número de passageiros deve estar entre 1 e 10")]
        public int NumeroPassageiros { get; set; }
        
        [Column(TypeName = "decimal(10,2)")]
        public decimal ValorTotalReserva { get; set; }
        
        [Column(TypeName = "decimal(10,2)")]
        public decimal DescontoAplicado { get; set; }
        
        public string StatusReserva { get; set; } = "Pendente";
        
        public string ObservacoesAdicionais { get; set; } = string.Empty;
        
        public DateTime? DataCancelamento { get; set; }
    }
}