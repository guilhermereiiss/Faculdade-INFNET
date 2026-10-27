from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "sqlite:///./clinica.db"
    secret_key: str = "troque-em-producao-clinica-medica-segura-2026-xyz"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Credenciais para integração M2M com o laboratório parceiro (Exercício 7)
    m2m_client_id: str = "laboratorio-parceiro-01"
    m2m_client_secret: str = "segredo-forte-m2m-lab-2026"
    
    # MFA simulado para conta de Administrador (Exercício 6)
    admin_mfa_secret: str = "CLINICA-MFA-2026"
    admin_mfa_default_totp: str = "123456"

    # CORS allowlist explícita (Exercício 10)
    allowed_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:5173",
        "https://app.clinicamedica.com.br",
        "https://laboratorio-parceiro.com.br",
    ]


settings = Settings()
