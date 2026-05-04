class InputNonZeroIntError(Exception):  # приклад створення власного класу виключення
    ERROR_COD_ZERO = 0  # задане число ціле, але нуль
    ERROR_CODE_NON_INTEGER = 1  # задано не ціле число

    def __init__(self, message, error_code, original_value):
        self.message = message
        self.error_code = error_code
        self.original_value = original_value

    def __str__(self):
        return self.message


def input_non_zero_int(message):
    """
    Користувацька функція введення цілого ненульового числа
    :param message: підказка для користувача
    :return: ціле число, або породжує виключення InputNonZeroIntError
    """
    s = input(message)
    try:
        n = int(s)
        if n == 0:
            raise InputNonZeroIntError("Задане число є нулем",
                                       InputNonZeroIntError.ERROR_COD_ZERO,
                                       s
                                       )
        return n
    except ValueError:  # перехоплюємо проблему задавання не цілого числа
        raise InputNonZeroIntError("Задане значення не є цілим числом",
                                   InputNonZeroIntError.ERROR_CODE_NON_INTEGER,
                                   s)


while True:
    try:
        n = input_non_zero_int("n = (int), (break to force exit)?")
        print(10 / n)  # тут може виникнути ділення на нуль
        break
    except InputNonZeroIntError as e:
        if e.error_code == InputNonZeroIntError.ERROR_CODE_NON_INTEGER and e.original_value == "break":
            break
            
        print(e)


# try:
#     n = int(input("n = (int)?")) # користувач може задати не ціле число
#     if n == 0:
#         raise MyZeroDivisionError("Ви задали число 0, на нуль культурні люди не ділять!")
#     print(10 / n) # тут може виникнути ділення на нуль
# except ValueError: # перехоплюємо проблему задавання не цілого числа
#     print("Ви мали задати ціле число")
# except MyZeroDivisionError as e: # перехоплюємо проблему ділення на нуль
#     print(e)
