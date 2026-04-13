def FactorialGenerator(): # нескінченний генератор
    i = 0
    factorial = 1 # 0!
    yield factorial
    while True:
        i += 1
        factorial *= i
        yield factorial




if __name__ == '__main__':
    for f in FactorialGenerator():
        print(f)
        if f > 1_000_000_000:
            break

