class Selector:
    def __init__(self, values):
        self.values = values

    def get_odds(self):
        return [x for x in self.values if x % 2 != 0]

    def get_evens(self):
        return [x for x in self.values if x % 2 == 0]


values = []
selector = Selector(values)
odds = selector.get_odds()
evens = selector.get_evens()
print(' '.join(map(str, odds)))
print(' '.join(map(str, evens)))