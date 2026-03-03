using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using AgenciaViagem.Models;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace AgenciaViagem.Pages
{
    public class IndexModel : PageModel
    {
        private readonly ILogger<IndexModel> _logger;
        private readonly AgenciaViagemContext _context;

        public IndexModel(ILogger<IndexModel> logger, AgenciaViagemContext context)
        {
            _logger = logger;
            _context = context;
            Pacotes = new List<PacoteTuristico>();
        }

        public IList<PacoteTuristico> Pacotes { get; set; }

        public async Task OnGetAsync()
        {
            Pacotes = await _context.PacotesTuristicos
                .Include(p => p.DestinosIncluidos)
                    .ThenInclude(d => d.PaisLocalizacao)
                .Include(p => p.ReservasEfetuadas)
                .Where(p => p.StatusAtivo && p.DataPartida > DateTime.Now)
                .ToListAsync();
        }
    }
}