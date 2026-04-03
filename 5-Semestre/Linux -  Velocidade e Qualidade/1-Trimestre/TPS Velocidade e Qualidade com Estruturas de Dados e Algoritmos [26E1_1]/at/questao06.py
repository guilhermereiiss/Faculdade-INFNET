class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self._length = 0

    def insert_first(self, value):
        new = Node(value)
        new.next = self.head
        self.head = new
        self._length += 1

    def insert_last(self, value):
        new = Node(value)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        self._length += 1

    def insert_at(self, index, value):
        if index < 0 or index > self._length:
            raise IndexError("Índice inválido")
        if index == 0:
            self.insert_first(value)
            return
        new = Node(value)
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        new.next = cur.next
        cur.next = new
        self._length += 1

    def search(self, value):
        cur = self.head
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

    def delete(self, value):
        if not self.head:
            return False
        if self.head.value == value:
            self.head = self.head.next
            self._length -= 1
            return True
        cur = self.head
        while cur.next:
            if cur.next.value == value:
                cur.next = cur.next.next
                self._length -= 1
                return True
            cur = cur.next
        return False

    def delete_at(self, index):
        if index < 0 or index >= self._length:
            raise IndexError("Índice inválido")
        if index == 0:
            self.head = self.head.next
            self._length -= 1
            return
        cur = self.head
        for _ in range(index - 1):
            cur = cur.next
        cur.next = cur.next.next
        self._length -= 1

    def __len__(self):
        return self._length

    def __str__(self):
        if not self.head:
            return "[]"
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.value))
            cur = cur.next
        return " -> ".join(res)

print("QUESTAO 6: ")
sll = SinglyLinkedList()
for i in range(5):
    sll.insert_last(i)
print("Lista:", sll)
sll.insert_at(2, 99)
print("Apos insert_at:", sll)
sll.delete_at(3)
print("Apos delete_at:", sll)