#  n    m    p
#  12   15 - порахувати найбільший спільний дільник двох натуральних чисел
#  15 % 12 = 3
#  12 %  3 = 0
#   3    0

n, m = [int(el) for el in input("n, m = ?").split()]
n1 = n
m1 = m
if n < m:  # сортуємо змінні n та m, так, щоб n >= m
    tmp = n
    n = m
    m = tmp

# print(n, m)

while m != 0:
    p = n % m
    # print(n, m, p)
    n = m
    m = p

print(f"gcd({n1}, {m1}) = {n}")


