cat > ex12_checklist_comissionamento.md << 'EOF'
# Exercício 12 - Checklist de Comissionamento de Conectividade

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M")  
**Sistema:** Kali Linux (VirtualBox)

## Checklist de Comissionamento (10 itens)

| # | Objetivo | Comando(s) | Evidência Esperada | Critério | Status |
|---|----------|------------|--------------------|----------|--------|
| 1 | Verificar endereço IPv6 | `ip -6 addr show eth0` | Endereço global + link-local | Tem ao menos 1 global + 1 link-local | **PASSOU** |
| 2 | Verificar rota default IPv6 | `ip -6 route \| grep default` | `default via fe80::2` | Existe rota default IPv6 | **PASSOU** |
| 3 | Verificar rota default IPv4 | `ip -4 route \| grep default` | Linha com "default via" | Existe rota default IPv4 | **FALHOU** |
| 4 | Verificar configuração DNS | `cat /etc/resolv.conf` | Nameserver configurado | Tem ao menos 1 nameserver | **PASSOU** |
| 5 | Verificar hostname | `hostname && hostnamectl` | Nome configurado | Hostname definido corretamente | **PASSOU** |
| 6 | Verificar portas TCP em escuta | `ss -tulpn \| grep LISTEN` | Lista de portas | Portas visíveis | **PASSOU** |
| 7 | Verificar uso de DHCP | `ip addr show eth0 \| grep dynamic` | Flag "dynamic" no IPv6 | Interface configurada via DHCP | **PASSOU** |
| 8 | Verificar forwarding IPv4 | `sysctl net.ipv4.ip_forward` | Valor = 0 | Forwarding desabilitado por padrão | **PASSOU** |
| 9 | Teste de conectividade básica | `ping -c 3 8.8.8.8` | Pacotes enviados/recebidos | Conectividade externa OK | **FALHOU** (sem IPv4) |
| 10 | Teste de resolução DNS | `getent hosts google.com` | IP resolvido | DNS funcionando | **PASSOU** |

---

## Evidências Reais dos Itens Executados (6+)

**Item 1 - IPv6 Address:**
```bash
$(ip -6 addr show eth0)