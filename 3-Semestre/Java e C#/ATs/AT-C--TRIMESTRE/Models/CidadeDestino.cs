using System.ComponentModel.DataAnnotations;

namespace AgenciaViagem.Models
{
    public class CidadeDestino
    {
        public int CidadeDestinoId { get; set; }
        
        [Required(ErrorMessage = "Nome da cidade é obrigatório")]
        [StringLength(100, MinimumLength = 3, ErrorMessage = "Nome da cidade deve ter entre 3 e 100 caracteres")]
        public string NomeCidade { get; set; } = string.Empty;
        
        public string DescricaoTuristica { get; set; } = string.Empty;
        
        public int PaisDestinoId { get; set; }
        public PaisDestino? PaisLocalizacao { get; set; }
        
        public bool StatusAtivo { get; set; } = true;
        
        public DateTime? DataExclusao { get; set; }
        
        public List<PacoteTuristico> PacotesIncluidos { get; set; } = new List<PacoteTuristico>();
    }
}