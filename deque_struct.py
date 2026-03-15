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

import test_deque
from deque_struct import Deque

# Основные тесты методов

def test_push_front():
    d = Deque(3)
    d.push_front(10)
    assert d.to_list() == [10]


def test_push_back():
    d = Deque(3)
    d.push_back(5)
    assert d.to_list() == [5]


def test_pop_front():
    d = Deque(3)
    d.push_back(1)
    assert d.pop_front() == 1
    assert d.is_empty()


def test_pop_back():
    d = Deque(3)
    d.push_back(2)
    assert d.pop_back() == 2
    assert d.is_empty()


def test_peek_front():
    d = Deque(3)
    d.push_back(7)
    assert d.peek_front() == 7


def test_peek_back():
    d = Deque(3)
    d.push_back(8)
    assert d.peek_back() == 8


def test_is_empty():
    d = Deque(2)
    assert d.is_empty()


def test_is_full():
    d = Deque(2)
    d.push_back(1)
    d.push_back(2)
    assert d.is_full()


def test_size():
    d = Deque(4)
    d.push_back(1)
    d.push_back(2)
    assert d.size() == 2


def test_to_list():
    d = Deque(4)
    d.push_back(10)
    d.push_back(20)
    d.push_front(5)
    assert d.to_list() == [5, 10, 20]

# Тесты крайних случаев:

def test_pop_empty():
    d = Deque(3)
    assert d.pop_front() is None
    assert d.pop_back() is None


def test_peek_empty():
    d = Deque(3)
    assert d.peek_front() is None
    assert d.peek_back() is None


def test_overflow():
    d = Deque(2)
    d.push_back(1)
    d.push_back(2)
    d.push_back(3)  # не должен добавиться
    assert d.to_list() == [1, 2]

from deque_struct import Deque

def main():
    d = Deque(4) # создадим дек с capacity = 4 (мах 4 элемента)

    # Тест 1: Добавление элементов
    d.push_back(10)
    d.push_back(20) # добавляем в конец списка 10 и 20 -> [10, 20]
    d.push_front(5) # и в начало 5
    print("Deque:", d.to_list())

    # Тест 2: Удаление элементов
    print("\npop_back ->", d.pop_back())
    print("Deque:", d.to_list())

    print("\npop_front ->", d.pop_front())
    print("Deque:", d.to_list())

    # Тест 3: Просмотр элементов без удаления
    print("\npeek_front ->", d.peek_front())
    print("peek_back ->", d.peek_back())

    # Тест 4: Проверка состояния
    print("\nis_empty ->", d.is_empty())
    print("size ->", d.size())

    # Тест 5: Заполнение до предела
    d.push_back(30)
    d.push_back(40)
    d.push_back(50) # добавим еще 3 числа, тк capacity=4, список станет полным: [10, 30, 40, 50]

    print("\nПосле добавления:", d.to_list())
    print("is_full ->", d.is_full()) # выдаст тру

    # Тест 6: Попытка добавить в полный дек
    d.push_back(60) #  предупреждение "Warning: дек полон"

if __name__ == "__main__":
    main()