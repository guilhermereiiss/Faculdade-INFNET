#!/bin/bash
openssl req -x509 -newkey rsa:2048 \
    -keyout servidor.key \
    -out servidor.crt \
    -days 365 \
    -nodes \
    -subj "/C=BR/ST=Bahia/L=Catu/O=AuditoriaSeguranca/CN=localhost"

echo ""
echo "Certificado gerado com sucesso:"
echo "  - servidor.crt (certificado)"
echo "  - servidor.key (chave privada)"