# По заданому набору трикутників, знайти той, що має найбільшу площу

class Triangle:
    def __init__(self, a, b, c):
        # перевірка чи такий трикутник існує???
        assert a + b > c and a + c > b and b + c > a, "Трикутник з такими сторонами не існує"
        self._a = a
        self._b = b
        self._c = c

    def get_a(self):
        return self._a

    def set_a(self, a):
        assert a + self._b > self._c and a + self._c > self._b and self._b + self._c > a, "Трикутник з такими сторонами не існує"
        self._a = a

    def get_c(self):
        return self._c

    def set_c(self, c):
        assert self._a + self._b > c and self._a + c > self._b and self._b + c > self._a, "Трикутник з такими сторонами не існує"
        self._c = c

    # алгоритми для одного трикутника ========
    def perimetr(self):
        return self._a + self._b + self._c

    def square(self):
        p = self.perimetr() / 2  # півпериметр
        s = p * (p - self._a) * (p - self._b) * (p - self._c)
        return s ** 0.5

    def __str__(self):  # для функції print
        return f"Triangle: a={self._a}, b={self._b}, c={self._c}"

########### MAIN ###############
if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    print(t)
    print(t.square())

    t.set_c(50)  # не можемо привести трикутник до неробочого стану, бо метод set_c автоматично перевіряє нерівність трикутника для значення яке ми хочемо встановити
    print(t)
    print(t.square())
    print(t.get_a())

