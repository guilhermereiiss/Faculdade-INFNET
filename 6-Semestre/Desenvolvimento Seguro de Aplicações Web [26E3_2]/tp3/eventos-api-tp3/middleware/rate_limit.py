from slowapi import Limiter
from slowapi.util import get_remote_address

# Limiter global — usa IP do cliente como chave
# Cada rota pode sobrescrever o limite com @limiter.limit("N/period")
limiter = Limiter(key_func=get_remote_address, default_limits=["60/minute"])
