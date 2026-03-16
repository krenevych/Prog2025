# По заданому набору трикутників, знайти той, що має найбільшу площу

class Triangle:
    def __init__(self, a, b, c):
        # перевірка чи такий трикутник існує???
        assert a + b > c and a + c > b and b + c > a, "Трикутник з такими сторонами не існує"
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

########### MAIN ###############
if __name__ == '__main__':
    t = Triangle(3, 4, 5)
    print(t)
    print(t.square())

    t.c = 50 # змінили стан нашого обʼєкту привівши його до не робочого варіанту
    print(t)
    print(t.square())

