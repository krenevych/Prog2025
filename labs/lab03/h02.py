n = int(input())

res = 0

# k = 0
pow = 1

while n > 0:
    c = n % 10

    if c % 2 == 0:
        c +=1
    else:
        c -= 1

    # res = 10**k * c + res
    res = pow * c + res

    n = n // 10
    # k += 1
    pow *= 10

print(res)
