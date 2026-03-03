using System.ComponentModel.DataAnnotations;

namespace AgenciaViagem.Models
{
    public class PaisDestino
    {
        public int PaisDestinoId { get; set; }
        
        [Required(ErrorMessage = "Nome do país é obrigatório")]
        [StringLength(50, MinimumLength = 3, ErrorMessage = "Nome do país deve ter entre 3 e 50 caracteres")]
        public string NomePais { get; set; } = string.Empty;
        
        [StringLength(5, ErrorMessage = "Código do país deve ter no máximo 5 caracteres")]
        public string CodigoPais { get; set; } = string.Empty;
        
        public string ContinenteLocalizacao { get; set; } = string.Empty;
        
        public bool StatusAtivo { get; set; } = true;
        
        public DateTime? DataExclusao { get; set; }
        
        public List<CidadeDestino> CidadesDisponiveis { get; set; } = new List<CidadeDestino>();
    }
}