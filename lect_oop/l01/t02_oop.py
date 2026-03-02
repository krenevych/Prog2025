# По заданому набору трикутників, знайти той, що має найбільшу площу

class Triangle:
    def __init__(self, a, b, c, id):
        # дані для одного трикутника!!!
        # перевірка чи такий трикутник існує???
        assert a + b > c and a + c > b and b + c > a
        self.a = a
        self.b = b
        self.c = c
        self.id = id  # ідентифікатор

    # алгоритми для одного трикутника ========
    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2  # півпериметр
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return s ** 0.5

    def h_a(self):
        return 100500

    def __str__(self):  # для функції print
        return f"Triangle: id={self.id}, a={self.a}, b={self.b}, c={self.c}"

    # алгоритми кінець ========


# дані початок ========
triangle_list = [
    [3, 4, 5],
    [5, 6, 5],
    [6, 7, 7],
    [1, 2, 100500]  # проблемні дані
]
# дані кінець ========

# створення трикутників
index = 0
triangles = []
for a, b, c in triangle_list:
    try:
        t = Triangle(a, b, c, index)  # t = Triangle(2, 3, 4)
        index += 1
        triangles.append(t)
    except AssertionError:
        # print("У списку є ʼпоганіʼ трикутники")
        pass

for t in triangles:
    print(t)
    print(t.square())
