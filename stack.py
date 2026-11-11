# Approach: wrap a Python list; the end of the list is the top of the stack.
# Time: push/pop/top/is_empty O(1) (push amortized, like vector::push_back)
# Space: O(n)

class Stack:
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty Stack")
        return self._data.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("top of empty Stack")
        return self._data[-1]

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"


if __name__ == "__main__":
    s = Stack()
    assert s.is_empty()

    for i in range(6):
        s.push(i * 10)

    assert len(s) == 6
    assert s.top() == 50
    assert s.pop() == 50
    assert repr(s) == "Stack([0, 10, 20, 30, 40])"

    while not s.is_empty():
        s.pop()

    try:
        s.pop()
        assert False, "should have raised"
    except IndexError:
        print("all tests passed")