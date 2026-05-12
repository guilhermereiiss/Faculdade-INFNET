# Exercício 1 - Runbook por Camadas: Diagnóstico de Conectividade no Linux

**Aluno:** [Seu Nome]  
**Hostname:** $(hostname)  
**Data:** $(date)  
**Distribuição:** Kali Linux (VirtualBox)

## Introdução
Este runbook organiza o diagnóstico de conectividade seguindo o modelo OSI/TCP-IP por camadas, permitindo identificar de forma sistemática onde está o problema de rede.

---

## 1. Enlace (Layer 1 / Layer 2)

**Comando 1:**
```bash
ip link show


