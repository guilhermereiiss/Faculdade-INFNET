def criptografar_cme(lista_pedidos, status="Pendente"):

    for codigo in lista_pedidos:
        mensagem = f"Pedido {codigo}: Status - {status}"
        mensagem_criptografada = ""

        for i, caractere in enumerate(mensagem):
            if caractere == " ":
                mensagem_criptografada += caractere
            elif i % 2 == 0:  
                mensagem_criptografada += chr(ord(caractere) + 2)
            else: 
                mensagem_criptografada += chr(ord(caractere) - 1)

        print(mensagem_criptografada)


def main09():
    pedidos = ["A123", "B456", "C789"]

    print("Teste com status padrão:")
    criptografar_cme(pedidos)

    print("\nTeste com status customizado:")
    criptografar_cme(pedidos, status="Enviado")


