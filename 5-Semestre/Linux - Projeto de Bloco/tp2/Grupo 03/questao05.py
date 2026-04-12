class No:
    def __init__(self, texto):
        self.texto = texto   # conteúdo da linha
        self.prev = None     # ponteiro para anterior
        self.next = None     # ponteiro para próxima


class ListaDupla:
    def __init__(self):
        self.head = None  # primeira linha
        self.tail = None  # última linha

    # Inserir nova linha no final
    def inserir(self, texto):
        novo = No(texto)

        if self.head is None:
            self.head = self.tail = novo
        else:
            self.tail.next = novo
            novo.prev = self.tail
            self.tail = novo

    # Remover uma linha pelo conteúdo
    def remover(self, texto):
        atual = self.head

        while atual:
            if atual.texto == texto:
                if atual.prev:
                    atual.prev.next = atual.next
                else:
                    self.head = atual.next

                if atual.next:
                    atual.next.prev = atual.prev
                else:
                    self.tail = atual.prev

                return
            atual = atual.next

    # Mostrar o texto completo
    def mostrar(self):
        atual = self.head
        while atual:
            print(atual.texto)
            atual = atual.next


# ============================
# Teste (simulando o editor)
# ============================

texto = ListaDupla()

texto.inserir("A natureza,")
texto.inserir("dizem-nos,")
texto.inserir("e apenas o habito...")
texto.inserir("(Rousseau)")

print("Texto original:\n")
texto.mostrar()

# Exemplo de remoção
print("\nRemovendo uma linha:\n")
texto.remover("dizem-nos,")
texto.mostrar()