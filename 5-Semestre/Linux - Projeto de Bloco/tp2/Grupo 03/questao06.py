class No:
    def __init__(self, texto):
        self.texto = texto
        self.prev = None
        self.next = None


class Editor:
    def __init__(self):
        self.head = None
        self.tail = None

    def to_list(self):
        arr = []
        atual = self.head
        while atual:
            arr.append(atual.texto)
            atual = atual.next
        return arr

    def from_list(self, arr):
        self.head = self.tail = None
        for linha in arr:
            self.inserir_final(linha)

    def inserir_final(self, texto):
        novo = No(texto)
        if not self.head:
            self.head = self.tail = novo
        else:
            self.tail.next = novo
            novo.prev = self.tail
            self.tail = novo

    def listar(self, i=None, f=None):
        arr = self.to_list()
        if i is None:
            i, f = 0, len(arr)-1
        for idx in range(i, f+1):
            print(f"{idx}: {arr[idx]}")

    def inserir(self, n=None):
        arr = self.to_list()
        if n is None:
            n = len(arr)-1

        print("Digite as linhas (digite 'FIM' para parar):")
        novas = []
        while True:
            linha = input()
            if linha == "FIM":
                break
            novas.append(linha)

        arr[n+1:n+1] = novas
        self.from_list(arr)

    def excluir(self, i=None, f=None):
        arr = self.to_list()
        if i is None:
            i = f = len(arr)-1
        del arr[i:f+1]
        self.from_list(arr)

    def duplicar(self, i, f, p):
        arr = self.to_list()
        bloco = arr[i:f+1]
        arr[p+1:p+1] = bloco
        self.from_list(arr)

    def alterar(self, n):
        arr = self.to_list()
        print("Nova linha:")
        arr[n] = input()
        self.from_list(arr)

    def carregar(self, arq, n=None):
        arr = self.to_list()
        if n is None:
            n = len(arr)-1

        with open(arq, "r") as f:
            linhas = f.read().splitlines()

        arr[n+1:n+1] = linhas
        self.from_list(arr)

    # SALVAR
    def salvar(self, arq, i=None, f=None):
        arr = self.to_list()
        if i is None:
            i, f = 0, len(arr)-1

        with open(arq, "w") as fobj:
            for linha in arr[i:f+1]:
                fobj.write(linha + "\n")

editor = Editor()

while True:
    comando = input("\nDigite comando: ")

    if comando.startswith("I"):
        partes = comando.split()
        n = int(partes[1]) if len(partes) > 1 else None
        editor.inserir(n)

    elif comando.startswith("E"):
        partes = comando[2:].split(",")
        if partes[0]:
            i = int(partes[0])
            f = int(partes[1])
            editor.excluir(i, f)
        else:
            editor.excluir()

    elif comando.startswith("D"):
        i, f, p = map(int, comando[2:].split(","))
        editor.duplicar(i, f, p)

    elif comando.startswith("L"):
        partes = comando[2:].split(",")
        if partes[0]:
            i = int(partes[0])
            f = int(partes[1])
            editor.listar(i, f)
        else:
            editor.listar()

    elif comando.startswith("C"):
        partes = comando[2:].split(",")
        arq = partes[0]
        n = int(partes[1]) if len(partes) > 1 else None
        editor.carregar(arq, n)

    elif comando.startswith("S"):
        partes = comando[2:].split(",")
        arq = partes[0]
        if len(partes) > 1:
            i = int(partes[1])
            f = int(partes[2])
            editor.salvar(arq, i, f)
        else:
            editor.salvar(arq)

    elif comando.startswith("A"):
        n = int(comando.split()[1])
        editor.alterar(n)

    elif comando == "F":
        print("Encerrando")
        break