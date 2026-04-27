

def exp(x, eps=0.0001):
    S = 1
    a = 1
    n = 0

    while abs(a) >= eps:  # |a| >= eps
        n += 1
        a *= x / n
        S = S + a

    return S


print(exp(3))

