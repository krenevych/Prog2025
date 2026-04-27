import math

# функція для обчислення sin
def sin_f(x, eps = 0.0001):
    a = x
    S = x
    k = 0

    while abs(a) >= eps:
        k += 1
        a *= - x*x / ((2 * k) * (2 * k + 1))
        S = S + a

    return S

# генератор для обчислення sin
def sin(x):
    a = x
    S = x
    k = 0
    yield S, a, k
    while True:
        k += 1
        a *= - x*x / ((2 * k) * (2 * k + 1))
        S = S + a
        yield S, a, k

####### головна програма
x = math.pi/3
for S, a, k in sin(x):
    # print(S, a, k)
    if abs(a) < 0.00001:
        print(S, k)
        print(math.sin(x))
        break