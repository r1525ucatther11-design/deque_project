from deque_struct import Deque

def main():
    d = Deque(4) # создадим дек с capacity = 4 (мах 4 элемента)

    # Тест 1: Добавление элементов
    print("Добавляем элементы")
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