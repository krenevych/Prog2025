class InputNonZeroIntError(Exception):  # базовий клас

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class InputNonIntError(InputNonZeroIntError):
    # задано не ціле число
    def __init__(self, original_value):
        super().__init__("Задане значення не є цілим числом")
        self.original_value = original_value

class InputZeroError(InputNonZeroIntError):
    # задане число ціле, але нуль
    def __init__(self):
        super().__init__("Задане число є нулем")

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
            raise InputZeroError

        return n
    except ValueError:  # перехоплюємо проблему задавання не цілого числа
        raise InputNonIntError(s)

if __name__ == '__main__':

    while True:
        try:
            n = input_non_zero_int("n = (int), (break to force exit)?")
            print(10 / n)  # тут може виникнути ділення на нуль
            break
        except InputNonIntError as e:
            if e.original_value == "break":
                break
            print(e)
        except InputZeroError as e:
            print(e)


