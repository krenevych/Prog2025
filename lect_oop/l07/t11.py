import math

x = float(input("x="))

S = 1
a = 1
n = 0

while abs(a) >= 0.001:  # |a| >= eps
    n += 1
    a *= x / n
    S = S + a

print(S, n)
print(math.exp(x))

