using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using AgenciaViagem.Models;
using System.Collections.Generic;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;

namespace AgenciaViagem.Pages.Clientes
{
    public class IndexModel : PageModel
    {
        private readonly AgenciaViagemContext _context;

        public IndexModel(AgenciaViagemContext context)
        {
            _context = context;
        }

        public IList<Cliente> Clientes { get; set; }

        [BindProperty]
        public string NomeCompleto { get; set; }

        [BindProperty]
        public string EnderecoEmail { get; set; }

        [BindProperty]
        public string NumeroTelefone { get; set; }

        [BindProperty]
        public int ClienteId { get; set; }

        public async Task OnGetAsync()
        {
            Clientes = await _context.Clientes
                .Where(c => c.StatusAtivo == true)
                .ToListAsync();
        }

        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            var novoCliente = new Cliente
            {
                NomeCompleto = NomeCompleto,
                EnderecoEmail = EnderecoEmail,
                NumeroTelefone = NumeroTelefone,
                DataCadastro = DateTime.Now,
                StatusAtivo = true
            };

            _context.Clientes.Add(novoCliente);
            await _context.SaveChangesAsync();

            return RedirectToPage();
        }

        public async Task<IActionResult> OnPostUpdateAsync()
        {
            if (!ModelState.IsValid)
            {
                Clientes = await _context.Clientes
                    .Where(c => c.StatusAtivo == true)
                    .ToListAsync();
                return Page();
            }

            var cliente = await _context.Clientes.FindAsync(ClienteId);
            if (cliente == null)
            {
                return NotFound();
            }

            cliente.NomeCompleto = NomeCompleto;
            cliente.EnderecoEmail = EnderecoEmail;
            cliente.NumeroTelefone = NumeroTelefone;

            await _context.SaveChangesAsync();
            return RedirectToPage();
        }

        public async Task<IActionResult> OnPostDeleteAsync(int id)
        {
            var cliente = await _context.Clientes.FindAsync(id);
            if (cliente == null)
            {
                return NotFound();
            }

            cliente.StatusAtivo = false;
            cliente.DataExclusao = DateTime.Now;
            await _context.SaveChangesAsync();

            return RedirectToPage();
        }
    }
}