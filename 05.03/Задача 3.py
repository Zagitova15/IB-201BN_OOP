from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self) -> int:
        pass


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: int):
        self.side = side

    def area(self) -> int:
        return self.side * self.side


def resize_rectangle(rect: Rectangle, width: int, height: int) -> int:
    rect.width = width
    rect.height = height
    return rect.area()


def resize_square(square: Square, side: int) -> int:
    square.side = side
    return square.area()