def check_password(required_password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_password = input("Введите пароль: ")
            if user_password != required_password:
                print("В доступе отказано")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@check_password('password')
def make_burger(typeOfMeat, withOnion=False, withTomato=True):
    return f"Бургер с {typeOfMeat}, лук: {withOnion}, томаты: {withTomato}"