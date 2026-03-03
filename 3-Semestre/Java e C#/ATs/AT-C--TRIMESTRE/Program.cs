using Microsoft.EntityFrameworkCore;
using System.IO;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();
builder.Services.AddDbContext<AgenciaViagemContext>(options =>
    options.UseSqlite("Data Source=agencia_viagem.db"));
builder.Services.AddAuthentication("CookieAuth")
    .AddCookie("CookieAuth", options =>
    {
        options.LoginPath = "/Login";
        options.AccessDeniedPath = "/AcessoNegado";
    });
builder.Services.AddAuthorization();

var app = builder.Build();

var filesPath = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot", "files");
if (!Directory.Exists(filesPath))
{
    Directory.CreateDirectory(filesPath);
}

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();
app.MapRazorPages();

app.Run();