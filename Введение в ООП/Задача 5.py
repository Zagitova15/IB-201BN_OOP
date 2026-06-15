class BigBell:
    def __init__(self):
        self.count = 0

    def sound(self):
        if self.count % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.count += 1

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()