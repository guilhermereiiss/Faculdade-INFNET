from slowapi import Limiter
from slowapi.util import get_remote_address

# Limitador baseado no endereço IP do cliente (Exercício 10)
# Protege contra ataques de força bruta, credential stuffing e DoS na API
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100/minute"],
    storage_uri="memory://",
)
