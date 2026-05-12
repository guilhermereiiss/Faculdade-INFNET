cat > ex9_portas_tcp.md << 'EOF'
# Exercício 9 - Portas TCP

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M")  
**Sistema:** Kali Linux (VirtualBox)

## 1. Portas TCP em Escuta

**Comando executado:**
```bash
ss -tulpn | grep LISTEN
tcp   LISTEN 0      1      [::ffff:127.0.0.1]:46445            *:*    users:(("java",pid=3297,fd=240))
tcp   LISTEN 0      50                  [::1]:34311         [::]:*    users:(("java",pid=3297,fd=22)) 
tcp   LISTEN 0      1      [::ffff:127.0.0.1]:42457            *:*    users:(("java",pid=3297,fd=325))
                                                                                                       