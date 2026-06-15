class Counter:
    def __init__(self, start: int = 0):
        self._value = start

    def inc(self):
        self._value += 1

    def dec(self):
        self._value -= 1

    def value(self) -> int:
        return self._value


class LimitedCounter(Counter):
    def __init__(self, min_value: int, max_value: int, start: int = 0):
        super().__init__(start)
        self.min_value = min_value
        self.max_value = max_value

    def inc(self):
        if self._value < self.max_value:
            super().inc()

    def dec(self):
        if self._value > self.min_value:
            super().dec()


if __name__ == "__main__":
    c = LimitedCounter(min_value=0, max_value=2)

    print(c.value())
    c.dec()
    print(c.value())

    c.inc()
    c.inc()
    c.inc()
    print(c.value())