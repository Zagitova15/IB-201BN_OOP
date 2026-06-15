class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __getitem__(self, index):
        return self.lst[-(index + 1)]


rl = ReversedList([10])
print(len(rl))
print(rl[0])