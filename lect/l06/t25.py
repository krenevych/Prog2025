import math



def table(func, xs):
    for x in xs:
        print(f"f({x})= {func(x)}")

def x2(x):
    return x*x

xs = [0, math.pi / 6, math.pi / 4,  math.pi / 3, math.pi / 2]
# table(math.sin, xs)
# table(math.cos, xs)
table(x2, [1, 2, 3, 4])