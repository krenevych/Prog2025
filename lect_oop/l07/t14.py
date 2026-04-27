def suma(): # нескінченний генератор
    S = 1
    n = 1
    yield S
    while True:
        n += 1
        S = S + 1/n
        yield S

if __name__ == '__main__':
    for S in suma():
        if S >= 15:
            print(S)
            break


