class Node:
    def __init__(self, palavra, significado):
        self.palavra = palavra
        self.significado = significado
        self.esq = None
        self.dir = None
        self.altura = 1


class AVLTree:
    def __init__(self):
        self.raiz = None
        self.tamanho = 0

    def altura(self, no):
        if not no:
            return 0
        return no.altura

    def balanceamento(self, no):
        if not no:
            return 0
        return self.altura(no.esq) - self.altura(no.dir)

    def rotacao_direita(self, y):
        x = y.esq
        T2 = x.dir

        x.dir = y
        y.esq = T2

        y.altura = 1 + max(self.altura(y.esq), self.altura(y.dir))
        x.altura = 1 + max(self.altura(x.esq), self.altura(x.dir))

        return x

    def rotacao_esquerda(self, x):
        y = x.dir
        T2 = y.esq

        y.esq = x
        x.dir = T2

        x.altura = 1 + max(self.altura(x.esq), self.altura(x.dir))
        y.altura = 1 + max(self.altura(y.esq), self.altura(y.dir))

        return y

    def inserir(self, palavra, significado):
        self.raiz = self._inserir(self.raiz, palavra, significado)

    def _inserir(self, no, palavra, significado):
        if not no:
            self.tamanho += 1
            return Node(palavra, significado)

        if palavra < no.palavra:
            no.esq = self._inserir(no.esq, palavra, significado)
        elif palavra > no.palavra:
            no.dir = self._inserir(no.dir, palavra, significado)
        else:
            no.significado = significado
            return no

        no.altura = 1 + max(self.altura(no.esq), self.altura(no.dir))
        balance = self.balanceamento(no)

        if balance > 1 and palavra < no.esq.palavra:
            return self.rotacao_direita(no)

        if balance < -1 and palavra > no.dir.palavra:
            return self.rotacao_esquerda(no)

        if balance > 1 and palavra > no.esq.palavra:
            no.esq = self.rotacao_esquerda(no.esq)
            return self.rotacao_direita(no)

        if balance < -1 and palavra < no.dir.palavra:
            no.dir = self.rotacao_direita(no.dir)
            return self.rotacao_esquerda(no)

        return no

    def buscar(self, palavra):
        return self._buscar(self.raiz, palavra)

    def _buscar(self, no, palavra):
        if not no:
            return None
        if palavra == no.palavra:
            return no.significado
        elif palavra < no.palavra:
            return self._buscar(no.esq, palavra)
        else:
            return self._buscar(no.dir, palavra)

    def listar(self):
        palavras = []
        self._em_ordem(self.raiz, palavras)
        return palavras

    def _em_ordem(self, no, lista):
        if no:
            self._em_ordem(no.esq, lista)
            lista.append((no.palavra, no.significado))
            self._em_ordem(no.dir, lista)

    def remover(self, palavra):
        self.raiz = self._remover(self.raiz, palavra)

    def _remover(self, no, palavra):
        if not no:
            return no

        if palavra < no.palavra:
            no.esq = self._remover(no.esq, palavra)
        elif palavra > no.palavra:
            no.dir = self._remover(no.dir, palavra)
        else:
            self.tamanho -= 1
            if not no.esq:
                return no.dir
            elif not no.dir:
                return no.esq

            temp = self._min_valor(no.dir)
            no.palavra = temp.palavra
            no.significado = temp.significado
            no.dir = self._remover(no.dir, temp.palavra)

        if not no:
            return no

        no.altura = 1 + max(self.altura(no.esq), self.altura(no.dir))
        balance = self.balanceamento(no)

        if balance > 1 and self.balanceamento(no.esq) >= 0:
            return self.rotacao_direita(no)

        if balance > 1 and self.balanceamento(no.esq) < 0:
            no.esq = self.rotacao_esquerda(no.esq)
            return self.rotacao_direita(no)

        if balance < -1 and self.balanceamento(no.dir) <= 0:
            return self.rotacao_esquerda(no)

        if balance < -1 and self.balanceamento(no.dir) > 0:
            no.dir = self.rotacao_direita(no.dir)
            return self.rotacao_esquerda(no)

        return no

    def _min_valor(self, no):
        atual = no
        while atual.esq:
            atual = atual.esq
        return atual

    def altura_arvore(self):
        return self.altura(self.raiz)

    def numero_itens(self):
        return self.tamanho


if __name__ == "__main__":
    dicionario = AVLTree()

    dicionario.inserir("python", "Linguagem de programacao")
    dicionario.inserir("arvore", "Estrutura de dados hierarquica")
    dicionario.inserir("algoritmo", "Sequencia de passos")

    print("Buscar 'python':", dicionario.buscar("python"))

    print("\nLista de palavras:")
    for palavra, significado in dicionario.listar():
        print(palavra, "->", significado)

    dicionario.remover("arvore")

    print("\nApos remocao:")
    for palavra, significado in dicionario.listar():
        print(palavra, "->", significado)

    print("\nAltura da arvore:", dicionario.altura_arvore())
    print("Numero de itens:", dicionario.numero_itens())