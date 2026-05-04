class MyZeroDivisionError(ZeroDivisionError): # приклад створення власного класу виключення
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:
    n = int(input("n = (int)?")) # користувач може задати не ціле число
    if n == 0:
        raise MyZeroDivisionError("Ви задали число 0, на нуль культурні люди не ділять!")
    print(10 / n) # тут може виникнути ділення на нуль
except ValueError: # перехоплюємо проблему задавання не цілого числа
    print("Ви мали задати ціле число")
except MyZeroDivisionError as e: # перехоплюємо проблему ділення на нуль
    print(e)

