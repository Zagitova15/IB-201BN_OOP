class User:
    _counter = 0

    def __init__(self, name: str, user_id: int):
        self.name = name
        self.id = user_id

    @classmethod
    def create(cls, name: str) -> "User":
        cls._counter += 1
        return cls(name, cls._counter)

    @classmethod
    def count(cls) -> int:
        return cls._counter


if __name__ == "__main__":
    u1 = User.create("Ann")
    u2 = User.create("Bob")
    u3 = User.create("Cory")
    print(u1.id, u2.id, u3.id)
    print(User.count())