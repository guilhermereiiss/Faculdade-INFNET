from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Exercício 6 — cabeçalhos de segurança HTTP aplicados a TODAS as respostas.

    HSTS: força HTTPS por 1 ano (evita downgrade para HTTP)
    X-Frame-Options: impede clickjacking via iframe
    X-Content-Type-Options: impede MIME sniffing (evita XSS via upload de arquivo)
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        return response
