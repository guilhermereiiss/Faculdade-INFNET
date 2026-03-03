using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using AgenciaViagem.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace AgenciaViagem.Pages.Reservas
{
    public class IndexModel : PageModel
    {
        private readonly AgenciaViagemContext _context;

        public IndexModel(AgenciaViagemContext context)
        {
            _context = context;
            Reservas = new List<Reserva>();
            Clientes = new List<Cliente>();
            PacotesDisponiveis = new List<PacoteTuristico>();
            Reserva = new Reserva();
        }

        public IList<Reserva> Reservas { get; set; }
        public IList<Cliente> Clientes { get; set; }
        public IList<PacoteTuristico> PacotesDisponiveis { get; set; }
        [BindProperty]
        public Reserva Reserva { get; set; }

        public async Task OnGetAsync()
        {
            Reservas = await _context.Reservas
                .Include(r => r.ClienteReservante)
                .Include(r => r.PacoteEscolhido)
                .ToListAsync();

            Clientes = await _context.Clientes
                .Where(c => c.StatusAtivo)
                .ToListAsync();

            PacotesDisponiveis = await _context.PacotesTuristicos
                .Include(p => p.ReservasEfetuadas)
                .Where(p => p.StatusAtivo && p.DataPartida > DateTime.Now)
                .ToListAsync();


            PacotesDisponiveis = PacotesDisponiveis
                .Where(p => p.CapacidadeMaximaViajantes -
                            (p.ReservasEfetuadas?.Count(r => r.StatusReserva == "Confirmada") ?? 0) > 0)
                .ToList();
        }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                await LoadSelectLists();
                return Page();
            }

          
            var existingReserva = await _context.Reservas
                .AnyAsync(r => r.ClienteId == Reserva.ClienteId &&
                               r.PacoteTuristicoId == Reserva.PacoteTuristicoId &&
                               r.StatusReserva == "Confirmada");

            if (existingReserva)
            {
                ModelState.AddModelError(string.Empty, "Este cliente já possui uma reserva confirmada para este pacote.");
                await LoadSelectLists();
                return Page();
            }


            var pacote = await _context.PacotesTuristicos
                .Include(p => p.ReservasEfetuadas)
                .FirstOrDefaultAsync(p => p.PacoteTuristicoId == Reserva.PacoteTuristicoId);

            if (pacote == null || !pacote.StatusAtivo || pacote.DataPartida <= DateTime.Now)
            {
                ModelState.AddModelError(string.Empty, "Pacote inválido ou não disponível.");
                await LoadSelectLists();
                return Page();
            }

            
            var vagasDisponiveis = pacote.CapacidadeMaximaViajantes - 
                                  (pacote.ReservasEfetuadas?.Count(r => r.StatusReserva == "Confirmada") ?? 0);
            if (Reserva.NumeroPassageiros > vagasDisponiveis)
            {
                ModelState.AddModelError(string.Empty, $"Capacidade insuficiente. Vagas disponíveis: {vagasDisponiveis}.");
                await LoadSelectLists();
                return Page();
            }

            
            Reserva.ValorTotalReserva = Reserva.NumeroPassageiros * pacote.ValorPorPessoa;
            Reserva.DataHoraReserva = DateTime.Now;
            Reserva.StatusReserva = "Confirmada"; 
            Reserva.DescontoAplicado = 0;

            _context.Reservas.Add(Reserva);
            await _context.SaveChangesAsync();

            pacote.VerificarCapacidadeDisponivel();

            TempData["CalculationData"] = JsonConvert.SerializeObject(new
            {
                numeroPassageiros = Reserva.NumeroPassageiros,
                valorPorPessoa = pacote.ValorPorPessoa,
                valorTotal = Reserva.ValorTotalReserva
            });

            return RedirectToPage();
        }

        private async Task LoadSelectLists()
        {
            Clientes = await _context.Clientes
                .Where(c => c.StatusAtivo)
                .ToListAsync();

            PacotesDisponiveis = await _context.PacotesTuristicos
                .Include(p => p.ReservasEfetuadas)
                .Where(p => p.StatusAtivo && p.DataPartida > DateTime.Now)
                .ToListAsync();

            PacotesDisponiveis = PacotesDisponiveis
                .Where(p => p.CapacidadeMaximaViajantes -
                            (p.ReservasEfetuadas?.Count(r => r.StatusReserva == "Confirmada") ?? 0) > 0)
                .ToList();
        }
    }
}
