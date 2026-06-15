class Temperature:
    @staticmethod
    def c_to_f(c: float) -> float:
        return round(c * 9/5 + 32, 2)

    @staticmethod
    def f_to_c(f: float) -> float:
        return round((f - 32) * 5/9, 2)


if __name__ == "__main__":
    print(Temperature.c_to_f(0))
    print(Temperature.f_to_c(212))
    print(Temperature.c_to_f(-40))
    print(Temperature.f_to_c(-40))