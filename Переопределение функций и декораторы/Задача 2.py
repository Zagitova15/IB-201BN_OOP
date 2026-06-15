def check_password(func):
    def wrapper(n):
        password = input("Введите пароль: ")
        if password != "secret":
            print("В доступе отказано")
            return None
        return func(n)
    return wrapper

@check_password
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)