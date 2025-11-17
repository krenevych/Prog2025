
a, b, c = [float(el) for el in input().split()]

# здійснити перевірку чи існує трикутник зі сторонами a, b, c

try:
    assert a + b > c and a + c > b and c + b > a, "трикутника з такими сторонами не існує"

    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    s = s ** 0.5

    print("Площа трикутника", s)
except AssertionError as err:
    print(err)


# рахувати площу по формулі Герона