cat > ex10_dhcp.md << 'EOF'
# Exercício 10 - DHCP

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M")  
**Sistema:** Kali Linux (VirtualBox)

## 1. Identificação se a interface usa DHCP

**Comando executado:**
```bash
ip addr show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:8a:35:d2 brd ff:ff:ff:ff:ff:ff
    inet6 fd17:625c:f037:2:2713:216d:9399:9a8a/64 scope global dynamic noprefixroute
       valid_lft 86297sec preferred_lft 14297sec
    inet6 fe80::cf4b:6e86:7b2d:d13a/64 scope link noprefixroute
       valid_lft forever preferred_lft forever