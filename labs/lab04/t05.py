n = int(input())


suma_tsifr = 0
dobutok_tsifr = 1
while n > 0:
    d = n % 10
    suma_tsifr = suma_tsifr + d
    dobutok_tsifr = dobutok_tsifr * d
    # print(d)
    n = n // 10

print(f"{(dobutok_tsifr / suma_tsifr):0.3f}")