n = int(input("n=? "))

# n = 234: 4 + 3 + 2 = 9
# 234 // 10 = 23 // 10 = 2 // 10 = 0

suma_digits = 0

while n > 0:
    d = n % 10
    n = n // 10
    suma_digits += d

print(suma_digits)