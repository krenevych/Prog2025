def suma(N):
    S = 1
    n = 1
    yield S
    while n < N + 1:
        n += 1
        S = S + 1/n
        yield S

if __name__ == '__main__':
    for S in suma(100):
        print(S)



