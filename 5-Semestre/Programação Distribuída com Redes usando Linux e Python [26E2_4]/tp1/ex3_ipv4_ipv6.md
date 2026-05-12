# Exercício 3 - IPv4 vs IPv6: Inventário e Prontidão Operacional

**Aluno:** Guilherme  
**Hostname:** $(hostname)  
**Data:** $(date +"%d/%m/%Y %H:%M:%S")  
**Sistema:** Kali Linux (VirtualBox)

## 1. Inventário de Endereços e Rotas

### IPv4

**Comando:** `ip -4 addr`
```bash
$(ip -4 addr)
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever

$(ip -6 addr)
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:8a:35:d2 brd ff:ff:ff:ff:ff:ff
    inet6 fd17:625c:f037:2:2713:216d:9399:9a8a/64 scope global dynamic noprefixroute
       valid_lft 86295sec preferred_lft 14295sec
    inet6 fe80::cf4b:6e86:7b2d:d13a/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
