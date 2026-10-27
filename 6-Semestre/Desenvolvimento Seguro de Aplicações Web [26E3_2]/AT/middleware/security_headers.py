from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Exercício 10 — Hardening de rede: cabeçalhos de segurança HTTP em todas as respostas.

    HSTS: Força conexões HTTPS por 1 ano, impedindo SSL stripping e downgrade attacks.
    X-Frame-Options: Impede que a aplicação seja renderizada em iframes (clickjacking).
    X-Content-Type-Options: Bloqueia ataques de MIME-sniffing.
    Referrer-Policy: Minimiza vazamento de dados confidenciais via cabeçalho Referer.
    Content-Security-Policy (CSP): Restringe a origem de scripts e recursos contra XSS.
    Permissions-Policy: Desabilita APIs de hardware não utilizadas (câmera, microfone, geolocalização).
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        response = await call_next(request)

        # 1. HSTS (HTTP Strict Transport Security)
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains; preload"

        # 2. Proteção contra Clickjacking
        response.headers["X-Frame-Options"] = "DENY"

        # 3. Prevenção de MIME-sniffing
        response.headers["X-Content-Type-Options"] = "nosniff"

        # 4. Política de Referrer
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"

        # 5. Content Security Policy (CSP)
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "script-src 'self'; "
            "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
            "font-src 'self' https://fonts.gstatic.com; "
            "img-src 'self' data:; "
            "frame-ancestors 'none'; "
            "form-action 'self';"
        )

        # 6. Desativação de permissões desnecessárias do navegador
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"

        return response
