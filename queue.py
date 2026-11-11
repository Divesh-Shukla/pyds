    # Approach: used a list to execute queue, the first element being the front and the last being the back
    # Time per op (enqueue / dequeue / front / is_empty): enqueue is O(1) and dequeue is O(n) too as the list is not contagious from what i know and front is O(1) and so is is_empty
    # Space: O(n)

    class Queue:
        def __init__(self):
            self._data = []

        def enqueue(self, element):
            self._data.append(element)
        
        def is_empty(self):
            return len(self._data) == 0
        
        def dequeue(self):
            if self.is_empty():
                raise IndexError("Queue is empty")
            else:
                return self._data.pop(0)

        def __len__(self):
            return len(self._data)

        def __repr__(self):
            return f"Queue{self._data[::-1]}"

        def front(self):
            if not self.is_empty():
                return self._data[0]
            else: 
                raise IndexError("Queue is empty")
        





    if __name__ == "__main__":
        import time

        def bench(n):
            q = Queue()
            for i in range(n):
                q.enqueue(i)
            start = time.perf_counter()
            while not q.is_empty():
                q.dequeue()
            return time.perf_counter() - start

        for n in (10_000, 20_000, 40_000, 80_000):
            print(n, bench(n))
