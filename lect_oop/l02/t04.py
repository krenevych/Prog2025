# По заданому набору трикутників, знайти той, що має найбільшу площу

class Triangle:

    class_name = "Triangle" # статичне поле класу Triangle, належить не конктретному екзепляру класу, а всьому класу загалом

    def __init__(self, a, b, c):
        # перевірка чи такий трикутник існує???
        assert self.is_exist(a, b, c), "Трикутник з такими сторонами не існує"
        self._a = a
        self._b = b
        self._c = c

    # def is_exist(self, a, b, c):
    #     # Бачимо, що в тілі цього методу ніде не трапляється self - посилання на поточний екземпляр
    #     return a + b > c and a + c > b and b + c > a

    @staticmethod
    def is_exist(a, b, c):
        # Бачимо, що в тілі цього методу ніде не трапляється self - посилання на поточний екземпляр
        return a + b > c and a + c > b and b + c > a

    def get_a(self):
        return self._a

    def set_a(self, a):
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

    check = Triangle.is_exist(34, 44, 54) # - чи існує трикутник зі сторонами 3, 4, 5
    print(check)
    if check:
        t2 = Triangle(34, 44, 54)
        print(t2.square())
        print(t2.class_name)

    print(Triangle.class_name)

    t = Triangle(3, 4, 5)
    print(t.class_name)

    Triangle.class_name = "Трикутник"
    # t.class_name = "Трикутник Привіт" # - cтворення поля class_name, що належить трикутнику t, не статичне
    print(t.class_name)
    print(t2.class_name)






