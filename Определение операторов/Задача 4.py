class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def days_in_month(self, month):
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_per_month[month - 1]

    def to_days(self):
        days = 0
        for m in range(1, self.month):
            days += self.days_in_month(m)
        days += self.day
        return days

    def __sub__(self, other):
        return self.to_days() - other.to_days()


mar5 = Date(3, 1)
jan1 = Date(1, 1)

print(mar5 - jan1)
print(jan1 - mar5)
print(jan1 - jan1)
print(mar5 - mar5)