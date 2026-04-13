def FactorialGenerator(n):
    factorial = 1 # 0!
    yield factorial
    # return 5 # - return як правило в генераторах не використовується
    for i in range(1, n + 1):
        factorial *= i
        yield factorial

    # yield "Все елементів більше не має"
    # yield "Не чіпай мене більше, я тобі сказав, більше нічого не лишилося"
    # yield "Нє, ну ти зовсім тупий, тобі ж сказано - все"



if __name__ == '__main__':
    # f = FactorialGenerator(5)
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    # print(next(f))
    for f in FactorialGenerator(5):
        print(f)
