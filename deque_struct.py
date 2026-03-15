class Deque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.count = 0

# Метод push_front(value) - добавить элемент в начало:
    def push_front(self, value):
        if self.is_full():
            print("Warning: дек полон")
            return

        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.count += 1

# Метод push_back(value) - добавить элемент в конец:
    def push_back(self, value):
        if self.is_full():
            print("Warning: дек полон")
            return

        index = (self.front + self.count) % self.capacity
        self.data[index] = value
        self.count += 1

# Метод pop_front() -> value | None - удалить и вернуть элемент из начала:
    def pop_front(self):
        if self.is_empty():
            return None

        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return val

# Метод pop_back() -> value | None - удалить и вернуть элемент с конца:
    def pop_back(self):
        if self.is_empty():
            return None

        index = (self.front + self.count - 1) % self.capacity
        val = self.data[index]
        self.data[index] = None
        self.count -= 1
        return val

# Метод peek_front() -> value | None - посмотреть первый элемент без удаления:
    def peek_front(self):
        if self.is_empty():
            return None
        return self.data[self.front]

# Метод peek_back() -> value | None - посмотреть последний элемент без удалени:
    def peek_back(self):
        if self.is_empty():
            return None
        index = (self.front + self.count - 1) % self.capacity
        return self.data[index]

    def is_empty(self):
        return self.count == 0 # is_empty() -> bool - проверить, пуст ли дек


    def is_full(self):
        return self.count == self.capacity # is_full() -> bool - проверить, заполнен ли дек

    def size(self):
        return self.count # size() -> int - текущее количество элементов

    def to_list(self): # to_list() -> list - вернуть элементы в правильном порядке
        result = []
        for i in range(self.count):
            index = (self.front + i) % self.capacity
            result.append(self.data[index])
        return result

    # Тест 6: Попытка добавить в полный дек
    d.push_back(60) #  предупреждение "Warning: дек полон"

if __name__ == "__main__":
    main()
