def func():
    a = 10 # локальна змінна
    b = 100  # локальна змінна

    print("func:", a, b)

    a = "hello"  # змінюємо локальну змінну a
    b = "world" # змінюємо глобальну змінну b

    print("func:", a, b)

def func2():
    a = "локальна у func2"

# MAIN
a = "глобальна змінна a"
b = "глобальна змінна b"

func()

print(a, b)
