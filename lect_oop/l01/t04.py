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

    def __str__(self):  # для функції print
        return f"Triangle: id={self.id}, a={self.a}, b={self.b}, c={self.c}"


t = Triangle(3, 4, 5, 911)
# print(t)
# print(t.square())








# дуже багато заплутаного коду







# ось тут ми маємо лише трикутник t і нам треба його копія


# t2 = Triangle()
t2 = t # ??? скопіювали трикутник ??? копіювання посилань!!! t2 це той же самий обʼєкт, що і t
print(f"t={t}")
print(f"t2={t2}")

t2.a = 100500

print(f"t={t}")
print(f"t2={t2}")

pass


