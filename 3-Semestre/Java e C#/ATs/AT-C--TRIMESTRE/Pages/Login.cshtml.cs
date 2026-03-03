using Microsoft.AspNetCore.Authentication;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using System.Security.Claims;
using System.Threading.Tasks;

namespace AgenciaViagem.Pages
{
    public class LoginModel : PageModel
    {
        [BindProperty]
        public string? usuario { get; set; }

        [BindProperty]
        public string? senha { get; set; }

        public async Task<IActionResult> OnPostAsync()
        {
            if (usuario == "admin" && senha == "12345")
            {
                var claims = new List<Claim>
                {
                    new Claim(ClaimTypes.Name, usuario)
                };
                var identidade = new ClaimsIdentity(claims, "CookieAuth");
                var principal = new ClaimsPrincipal(identidade);

                await HttpContext.SignInAsync("CookieAuth", principal);

                return RedirectToPage("/Index");
            }

            ModelState.AddModelError("", "Credenciais inválidas");
            return Page();
        }
    }
}