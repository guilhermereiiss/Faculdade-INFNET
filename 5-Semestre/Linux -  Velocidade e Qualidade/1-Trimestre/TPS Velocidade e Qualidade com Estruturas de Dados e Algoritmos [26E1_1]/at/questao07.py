class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def insert_first(self, value):
        new = DoublyNode(value)
        if not self.head:
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self._length += 1

    def insert_last(self, value):
        new = DoublyNode(value)
        if not self.tail:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self._length += 1

    def delete_first(self):
        if not self.head:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._length -= 1

    def delete_last(self):
        if not self.tail:
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._length -= 1

    def is_empty(self):
        return self._length == 0

class Deque:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def insert_left(self, v):
        self.dll.insert_first(v)

    def insert_right(self, v):
        self.dll.insert_last(v)

    def remove_left(self):
        if self.dll.is_empty():
            raise IndexError("Deque vazio")
        v = self.dll.head.value
        self.dll.delete_first()
        return v

    def remove_right(self):
        if self.dll.is_empty():
            raise IndexError("Deque vazio")
        v = self.dll.tail.value
        self.dll.delete_last()
        return v

    def peek_left(self):
        if self.dll.is_empty():
            raise IndexError("Deque vazio")
        return self.dll.head.value

    def peek_right(self):
        if self.dll.is_empty():
            raise IndexError("Deque vazio")
        return self.dll.tail.value

print("QUESTAO 7: ")
dq = Deque()
for x in [5, 10, 1]:
    dq.insert_left(x)
for x in [20, 30]:
    dq.insert_right(x)
print("remove_right:", dq.remove_right())
print("remove_left:", dq.remove_left())