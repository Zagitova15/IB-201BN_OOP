class Password:
    @staticmethod
    def is_strong(p: str) -> bool:
        if len(p) < 8:
            return False

        has_digit = any(char.isdigit() for char in p)
        has_upper = any(char.isupper() for char in p)
        has_lower = any(char.islower() for char in p)

        return has_digit and has_upper and has_lower


if __name__ == "__main__":
    print(Password.is_strong('qwerty'))
    print(Password.is_strong('Qwerty12'))
    print(Password.is_strong('QWERTY12'))
    print(Password.is_strong('Qwerty123'))