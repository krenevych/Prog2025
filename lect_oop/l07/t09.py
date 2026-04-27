import math

x = float(input("x="))
N = int(input("N="))

S = 1
a = 1
n = 0
# замінили цикл for циклом while
while n < N + 1:
    n += 1
    a *= x / n
    S = S + a

print(S)
print(math.exp(x))

