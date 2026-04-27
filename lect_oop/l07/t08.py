import math

x = float(input("x="))
N = int(input("N="))

S = 1
a = 1

for n in range(1, N+1):
    a *= x / n
    S = S + a

print(S)
print(math.exp(x))

