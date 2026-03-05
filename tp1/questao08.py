def bubbleSort(self):
    left = 0
    right = self.__nItems - 1

    while left < right:

        # Da esquerda para a direita
        for i in range(left, right):
            if self.__a[i] > self.__a[i + 1]:
                self.swap(i, i + 1)

        right -= 1  

        # Da direita para a esquerda
        for i in range(right, left, -1):
            if self.__a[i] < self.__a[i - 1]:
                self.swap(i, i - 1)

        left += 1 
