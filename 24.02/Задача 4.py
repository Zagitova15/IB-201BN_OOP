import math


class Point:
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    @classmethod
    def from_string(cls, s: str) -> "Point":
        # Убираем пробелы и разделяем по запятой
        parts = s.replace(" ", "").split(",")
        return cls(float(parts[0]), float(parts[1]))

    @classmethod
    def from_dict(cls, d: dict) -> "Point":
        return cls(d["x"], d["y"])

    @staticmethod
    def distance(a: "Point", b: "Point") -> float:
        return round(math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2), 2)


if __name__ == "__main__":
    p1 = Point.from_string("3, 4")
    p2 = Point.from_dict({"x": 0, "y": 0})
    print(p1.x, p1.y)
    print(Point.distance(p1, p2))