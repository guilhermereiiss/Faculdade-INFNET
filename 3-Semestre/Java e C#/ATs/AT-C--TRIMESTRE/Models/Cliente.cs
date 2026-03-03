using System.ComponentModel.DataAnnotations;

namespace AgenciaViagem.Models
{
    public class Cliente
    {
        public int ClienteId { get; set; }
        
        [Required(ErrorMessage = "Nome é obrigatório")]
        [StringLength(100, MinimumLength = 3, ErrorMessage = "Nome deve ter entre 3 e 100 caracteres")]
        public string NomeCompleto { get; set; } = string.Empty;
        
        [Required(ErrorMessage = "Email é obrigatório")]
        [EmailAddress(ErrorMessage = "Email inválido")]
        public string EnderecoEmail { get; set; } = string.Empty;
        
        [Phone(ErrorMessage = "Telefone inválido")]
        public string NumeroTelefone { get; set; } = string.Empty;
        
        public DateTime DataCadastro { get; set; }
        
        public bool StatusAtivo { get; set; } = true;
        
        public DateTime? DataExclusao { get; set; }
        
        public List<Reserva> ReservasRealizadas { get; set; } = new List<Reserva>();
    }
}