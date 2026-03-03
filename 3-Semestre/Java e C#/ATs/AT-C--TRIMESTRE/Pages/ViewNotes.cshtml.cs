using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Threading.Tasks;

namespace AgenciaViagem.Pages
{
    public class ViewNotesModel : PageModel
    {
        private readonly string _filesPath;

        public ViewNotesModel(IWebHostEnvironment env)
        {
            _filesPath = Path.Combine(env.WebRootPath, "files");
            ArquivosNotas = new List<string>();
            ConteudoVisualizado = string.Empty;
        }

        [BindProperty]
        public string? conteudoNota { get; set; }

        public List<string> ArquivosNotas { get; set; }
        public string ConteudoVisualizado { get; set; }

        public void OnGet()
        {
            CarregarArquivos();
        }

        public async Task<IActionResult> OnPostCriarNotaAsync()
        {
            if (!string.IsNullOrEmpty(conteudoNota))
            {
                var nomeArquivo = $"nota_{DateTime.Now:yyyyMMddHHmmss}.txt";
                var caminhoArquivo = Path.Combine(_filesPath, nomeArquivo);
                await System.IO.File.WriteAllTextAsync(caminhoArquivo, conteudoNota);
            }
            return RedirectToPage();
        }

        public IActionResult OnGetVisualizar(string arquivo)
        {
            if (string.IsNullOrEmpty(arquivo))
            {
                return NotFound();
            }

            var caminhoArquivo = Path.Combine(_filesPath, arquivo);
            if (!System.IO.File.Exists(caminhoArquivo))
            {
                return NotFound();
            }

            ConteudoVisualizado = System.IO.File.ReadAllText(caminhoArquivo);
            CarregarArquivos();
            return Page();
        }

        private void CarregarArquivos()
        {
            if (Directory.Exists(_filesPath))
            {
                ArquivosNotas = Directory.GetFiles(_filesPath, "*.txt").ToList();
            }
            else
            {
                ArquivosNotas = new List<string>();
            }
        }
    }
}