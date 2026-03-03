using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace AgenciaViagem.Models
{
    public class PacoteTuristico
    {
        public int PacoteTuristicoId { get; set; }
        
        [Required(ErrorMessage = "Título é obrigatório")]
        [StringLength(200, MinimumLength = 5, ErrorMessage = "Título deve ter entre 5 e 200 caracteres")]
        public string TituloPacote { get; set; } = string.Empty;
        
        public string DescricaoCompleta { get; set; } = string.Empty;
        
        [Required(ErrorMessage = "Data de início é obrigatória")]
        public DateTime DataPartida { get; set; }
        
        [Required(ErrorMessage = "Data de término é obrigatória")]
        public DateTime DataRetorno { get; set; }
        
        [Required(ErrorMessage = "Capacidade máxima é obrigatória")]
        [Range(1, 100, ErrorMessage = "Capacidade deve estar entre 1 e 100")]
        public int CapacidadeMaximaViajantes { get; set; }
        
        [Required(ErrorMessage = "Preço é obrigatório")]
        [Column(TypeName = "decimal(10,2)")]
        [Range(0.01, 999999.99, ErrorMessage = "Preço deve estar entre 0.01 e 999999.99")]
        public decimal ValorPorPessoa { get; set; }
        
        public int NumeroDiarias { get; set; }
        
        public bool StatusAtivo { get; set; } = true;
        
        public DateTime? DataExclusao { get; set; }
        
        public List<CidadeDestino> DestinosIncluidos { get; set; } = new List<CidadeDestino>();
        
        public List<Reserva> ReservasEfetuadas { get; set; } = new List<Reserva>();
        
        public event EventHandler? LimiteCapacidadeAtingido;
        
        public void VerificarCapacidadeDisponivel()
        {
            if (ReservasEfetuadas != null && ReservasEfetuadas.Where(r => r.StatusReserva == "Confirmada").Count() >= CapacidadeMaximaViajantes)
            {
                LimiteCapacidadeAtingido?.Invoke(this, EventArgs.Empty);
            }
        }
        
        public int ObterVagasDisponiveis()
        {
            var reservasConfirmadas = ReservasEfetuadas?.Where(r => r.StatusReserva == "Confirmada").Count() ?? 0;
            return CapacidadeMaximaViajantes - reservasConfirmadas;
        }
    }
}   