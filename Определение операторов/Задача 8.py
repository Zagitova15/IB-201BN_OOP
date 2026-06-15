class Queue:
    def __init__(self, *values):
        self.items = list(values)

    def append(self, *values):
        self.items.extend(values)

    def copy(self):
        new_queue = Queue()
        new_queue.items = self.items.copy()
        return new_queue

    def pop(self):
        if self.items:
            return self.items.pop(0)
        return None

    def extend(self, queue):
        self.items.extend(queue.items)

    def next(self):
        return Queue(*self.items[1:])

    def __add__(self, other):
        new_queue = self.copy()
        new_queue.extend(other)
        return new_queue

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self.items == other.items

    def __rshift__(self, n):
        if n >= len(self.items):
            return Queue()
        return Queue(*self.items[n:])

    def __str__(self):
        if not self.items:
            return "[]"
        return "[" + " -> ".join(str(item) for item in self.items) + "]"

    def __next__(self):
        return self.next()


q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep='\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)