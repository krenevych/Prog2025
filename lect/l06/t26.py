
def table(func, xs):
    for x in xs:
        print(f"f({x})= {func(x)}") # здійснюємо виклик, для функції func, що прийшла у якості параметра.

##### MAIN ######
print("Таблиця значень для функції x**2:")
table(lambda x: x ** 2, [1, 2, 3, 4])

print("Таблиця значень для функції x**3:")
table(lambda x: x**3, [1, 2, 3, 4])