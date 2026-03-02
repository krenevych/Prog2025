# По заданому набору трикутників, знайти той, що має найбільшу площу

# алгоритми початок ========
def perimetr(a, b, c):
    return a + b + c


def square(a, b, c):
    p = perimetr(a, b, c) / 2  # півпериметр
    s = p * (p - a) * (p - b) * (p - c)
    return s ** 0.5
# алгоритми кінець ========

# дані початок ========
triangle_list = [
    [3, 4, 5],
    [5, 6, 5],
    [6, 7, 7],
    [1, 2, 100500]  # проблемні дані
]
# дані кінець ========

max_square = 0
max_index = -1
index = 0
for a, b, c in triangle_list:
    # перевірка чи такий трикутник існує???
    if a + b > c and a + c > b and b + c > a:
        s = square(a, b, c)
        if max_square < s:
            max_square = s
            max_index = index

        index+=1
        print(s)

print(max_index, max_square)
