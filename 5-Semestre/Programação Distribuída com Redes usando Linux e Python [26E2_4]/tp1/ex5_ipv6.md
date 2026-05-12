cat > ex5_ipv6.md << 'EOF'
# Exercício 5 - Configuração IPv6

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M")  
**Sistema:** Kali Linux (VirtualBox)

## 1. Comandos Executados

**Comando:** `ip -6 addr show`
```bash
$(ip -6 addr show)
fd17:625c:f037:2::/64 dev eth0 proto ra metric 100 pref medium
fe80::/64 dev eth0 proto kernel metric 1024 pref medium
default via fe80::2 dev eth0 proto ra metric 100 pref medium

**Comando 1:** `ip -6 addr show`
```bash
$(ip -6 addr show)