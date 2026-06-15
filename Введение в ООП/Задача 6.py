class MinMaxWordFinder:
    def __init__(self):
        self.words = []
        self.min_len = float('inf')
        self.max_len = 0
        self.longest_words_set = set()

    def add_sentence(self, sentence):
        new_words = sentence.split()
        self.words.extend(new_words)

        for word in new_words:
            if len(word) < self.min_len:
                self.min_len = len(word)
            if len(word) > self.max_len:
                self.max_len = len(word)

        self.longest_words_set.clear()
        for word in self.words:
            if len(word) == self.max_len:
                self.longest_words_set.add(word)

    def shortest_words(self):
        result = [word for word in self.words if len(word) == self.min_len]
        result.sort()
        return result

    def longest_words(self):
        result = sorted(self.longest_words_set)
        return result

finder = MinMaxWordFinder()
finder.add_sentence('hello')
finder.add_sentence('  abc     def    ')
finder.add_sentence('world')
finder.add_sentence('            abc          ')
finder.add_sentence('asdf')
finder.add_sentence('qwert')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))