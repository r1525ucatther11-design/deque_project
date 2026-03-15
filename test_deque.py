from deque_struct import Deque

# Тесты методов
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