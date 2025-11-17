# знайти розвʼязок рівння ax + b = 0

a, b = [float(el) for el in input().split()]

if a != 0:
    x = b / a  # логічна помилка, бо x = -b / a
    print(x)
else:
    print("розвʼязку не існує")