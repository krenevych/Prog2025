def suma(): # нескінченний генератор
    S = 1
    n = 1
    yield S, n
    while True:
        n += 1
        S = S + 1/n
        yield S, n

if __name__ == '__main__':
    for S, n in suma():
        if S >= 16:
            print(S, n)
            break


