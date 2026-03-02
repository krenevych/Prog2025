# По заданому набору трикутників, знайти той, що має найбільшу площу

class Triangle:
    def __init__(self, a, b, c, id):
        # дані для одного трикутника!!!
        # перевірка чи такий трикутник існує???
        assert a + b > c and a + c > b and b + c > a
        self.a = a
        self.b = b
        self.c = c
        self.id = id # ідентифікатор

    # алгоритми для одного трикутника ========
    def perimetr(self):
        return self.a + self.b + self.c


    def square(self):
        p = self.perimetr() / 2  # півпериметр
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return s ** 0.5

    def __str__(self): # для функції print
        return f"Triangle: {self.id=}, {self.a=}, {self.b=}, {self.c=}"

    # алгоритми кінець ========



# дані початок ========
triangle_list = [
    [3, 4, 5],
    [5, 6, 5],
    [6, 7, 7],
    [1, 2, 100500]  # проблемні дані
]
# дані кінець ========

t1 = Triangle(3, 4, 5, 1)
print(t1.square())

t2 = Triangle(4, 5, 6, 2)
print(t2.square())

print(t1)
print(t2)


# for a, b, c in triangle_list:
#    t = Triangle(a, b, c)  # t = Triangle(2, 3, 4)
