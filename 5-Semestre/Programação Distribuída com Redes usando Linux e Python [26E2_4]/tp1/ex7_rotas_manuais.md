cat > ex7_rotas_manuais.md << 'EOF'
# Exercício 7 - Rotas Manuais

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M")  
**Sistema:** Kali Linux (VirtualBox)

## 1. Estado Inicial

**Comando:** `ip -6 route`
```bash
fd17:625c:f037:2::/64 dev eth0 proto ra metric 100 pref medium
fe80::/64 dev eth0 proto kernel metric 1024 pref medium
default via fe80::2 dev eth0 proto ra metric 100 pref medium