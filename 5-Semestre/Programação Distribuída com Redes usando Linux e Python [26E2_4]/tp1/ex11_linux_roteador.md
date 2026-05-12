cat > ex11_linux_roteador.md << 'EOF'
# Exercício 11 - Linux como Roteador

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M")  
**Sistema:** Kali Linux (VirtualBox)

## 1. Verificação do Estado Atual do Forwarding

**Comando executado:**
```bash
sysctl net.ipv4.ip_forward
┌──(kali㉿kali)-[~/…/Faculdade-INFNET/5-Semestre/Programação Distribuída com Redes usando Linux e Python [26E2_4]/tp1]
└─$ sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 0
                                                                                                                                                           
┌──(kali㉿kali)-[~/…/Faculdade-INFNET/5-Semestre/Programação Distribuída com Redes usando Linux e Python [26E2_4]/tp1]
└─$ sudo sysctl -w net.ipv4.ip_forward=1
sudo: unable to resolve host kali: Name or service not known
[sudo] password for kali: 
net.ipv4.ip_forward = 1
                                                                                                                                                           
┌──(kali㉿kali)-[~/…/Faculdade-INFNET/5-Semestre/Programação Distribuída com Redes usando Linux e Python [26E2_4]/tp1]
└─$ sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 1
                                                                                                                                                           
┌──(kali㉿kali)-[~/…/Faculdade-INFNET/5-Semestre/Programação Distribuída com Redes usando Linux e Python [26E2_4]/tp1]
└─$ sudo sysctl -w net.ipv4.ip_forward=0
sudo: unable to resolve host kali: Name or service not known
net.ipv4.ip_forward = 0
                                                                                                                                                           
┌──(kali㉿kali)-[~/…/Faculdade-INFNET/5-Semestre/Programação Distribuída com Redes usando Linux e Python [26E2_4]/tp1]
└─$ sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 0
