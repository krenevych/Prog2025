
while True:
    a, b, c = [float(el) for el in input("Задайте сторони трикутника ").split()]
    try:
         assert a + b > c and a + c > b and b + c > a

         # print(a, b, c)
         p = (a + b + c) / 2

         s = p * (p - a) * (p - b) * (p - c)

         print(s**0.5)

    except AssertionError:
        print("Задайте сторони трикутника правильно (нерівність трикутника має виконуватися!)")
    else:
        break
