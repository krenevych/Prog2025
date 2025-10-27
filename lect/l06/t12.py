def func(param1, param2, param3):
    print(f"{param1=}")
    print(f"{param2=}")
    print(f"{param3=}")

#### MAIN #######

# func(3, 2, 8)  # приклад використання позиційних параметрів
# func(param1=3, param2=2, param3=8)  # явно вказуємо яке значення фактичного аргументу підставити до формального параметру
func(param3=8, param2=2,  param1=3)  # використання ключових параметрів