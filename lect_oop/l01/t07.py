# По заданому набору трикутників, знайти той, що має найбільшу площу
from __future__ import annotations

class Triangle:
    def __init__(self, a: float | int | Triangle, b=None, c=None):
        # if a - це екземпляр класу Triangle:
        #     a.a, a.b, a.c
        if isinstance(a, Triangle):
            self.a = a.a
            self.b = a.b
            self.c = a.c
        else:
            assert a + b > c and a + c > b and b + c > a
            self.a = a
            self.b = b
            self.c = c

    # алгоритми для одного трикутника ========
    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = self.perimetr() / 2  # півпериметр
        s = p * (p - self.a) * (p - self.b) * (p - self.c)
        return s ** 0.5

    def __str__(self):  # для функції print
        return f"Triangle: a={self.a}, b={self.b}, c={self.c}"


t = Triangle(3, 4, 5)
# t3 = Triangle("three", 4, 5)

t2 = Triangle(t)  # тут хочемо, щоб працював конструктор копіювання

print(t)
print(t2)


