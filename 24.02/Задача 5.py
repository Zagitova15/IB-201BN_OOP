class Shape:
    _registry = {}

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        # Регистрируем подкласс
        Shape._registry[cls.__name__] = cls

    @classmethod
    def available(cls) -> list[str]:
        return sorted(cls._registry.keys())

class Circle(Shape):
    pass


class Square(Shape):
    pass


class Triangle(Shape):
    pass


if __name__ == "__main__":
    print(Shape.available())