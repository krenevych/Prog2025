# По заданому набору трикутників, знайти той, що має найбільшу площу

class Triangle:

    def __init__(self, a, b, c):
        # перевірка чи такий трикутник існує???
        assert self.is_exist(a, b, c), "Трикутник з такими сторонами не існує"
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_exist(a, b, c):
        # Бачимо, що в тілі цього методу ніде не трапляється self - посилання на поточний екземпляр
        return a + b > c and a + c > b and b + c > a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        assert self.is_exist(a, self._b, self._c), "Трикутник з такими сторонами не існує"
        self._a = a

    def get_c(self):
        return self._c

    def set_c(self, c):
        assert self.is_exist(self._a, self._b, c), "Трикутник з такими сторонами не існує"
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
    print(t.a)
    t.a = 4
    print(t.a)
    print(t)






