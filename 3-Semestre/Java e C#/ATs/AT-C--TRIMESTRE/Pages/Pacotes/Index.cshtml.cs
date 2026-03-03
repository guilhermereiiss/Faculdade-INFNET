using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using AgenciaViagem.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace AgenciaViagem.Pages.Pacotes
{
    public class IndexModel : PageModel
    {
        private readonly AgenciaViagemContext _context;

        public IndexModel(AgenciaViagemContext context)
        {
            _context = context;
            Pacotes = new List<PacoteTuristico>();
            CidadesDisponiveis = new List<CidadeDestino>();
            Pacote = new PacoteTuristico();
            SelectedCidadeIds = new List<int>();
        }

        public IList<PacoteTuristico> Pacotes { get; set; }
        public IList<CidadeDestino> CidadesDisponiveis { get; set; }
        [BindProperty]
        public PacoteTuristico Pacote { get; set; }
        [BindProperty]
        public List<int> SelectedCidadeIds { get; set; }

        public async Task OnGetAsync()
        {
            Pacotes = await _context.PacotesTuristicos
                .Include(p => p.DestinosIncluidos)
                .Include(p => p.ReservasEfetuadas)
                .Where(p => p.StatusAtivo && p.DataPartida > DateTime.Now)
                .ToListAsync();

            CidadesDisponiveis = await _context.CidadesDestinos
                .Include(c => c.PaisLocalizacao)
                .Where(c => c.StatusAtivo)
                .ToListAsync();
        }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                CidadesDisponiveis = await _context.CidadesDestinos
                    .Include(c => c.PaisLocalizacao)
                    .Where(c => c.StatusAtivo)
                    .ToListAsync();
                return Page();
            }

            Pacote.StatusAtivo = true;
            Pacote.NumeroDiarias = (Pacote.DataRetorno - Pacote.DataPartida).Days;

            if (SelectedCidadeIds != null && SelectedCidadeIds.Any())
            {
                Pacote.DestinosIncluidos = await _context.CidadesDestinos
                    .Where(c => SelectedCidadeIds.Contains(c.CidadeDestinoId))
                    .ToListAsync();
            }

            _context.PacotesTuristicos.Add(Pacote);
            await _context.SaveChangesAsync();

            return RedirectToPage();
        }
    }
}