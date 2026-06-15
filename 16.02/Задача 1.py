class User:
    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    @property
    def username(self):
        return self._username

    def check_password(self, password: str) -> bool:
        return self._password == password

    def set_password(self, old_password: str, new_password: str) -> bool:
        if self.check_password(old_password):
            self._password = new_password
            return True
        return False


if __name__ == "__main__":
    u = User("alice", "1234")

    print(u.username)
    print(u.check_password("0000"))
    print(u.check_password("1234"))

    print(u.set_password("0000", "abcd"))
    print(u.set_password("1234", "abcd"))
    print(u.check_password("abcd"))