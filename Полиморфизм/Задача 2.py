class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.line = []
        self.current_length = 0

    def add_word(self, word):
        if self.current_length + len(word) + (1 if self.line else 0) <= self.width:
            if self.line:
                self.line.append(word)
                self.current_length += len(word) + 1
            else:
                self.line.append(word)
                self.current_length += len(word)
        else:
            self.end()
            self.line.append(word)
            self.current_length = len(word)

    def end(self):
        if self.line:
            print(' '.join(self.line))
            self.line = []
            self.current_length = 0


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.line = []
        self.current_length = 0

    def add_word(self, word):
        if self.current_length + len(word) + (1 if self.line else 0) <= self.width:
            if self.line:
                self.line.append(word)
                self.current_length += len(word) + 1
            else:
                self.line.append(word)
                self.current_length += len(word)
        else:
            self.end()
            self.line.append(word)
            self.current_length = len(word)

    def end(self):
        if self.line:
            line_str = ' '.join(self.line)
            print(' ' * (self.width - len(line_str)) + line_str)
            self.line = []
            self.current_length = 0


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()