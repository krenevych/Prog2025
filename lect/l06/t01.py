# Дано список натуральних чисел.
# Визначити ті з них які є простими числами

# lst = [int(el) for el in input("Задайте список натуральних чисел ").split()]
lst = [45, 13, 7, 16, 113, 5]

for n in lst:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    # print(f"те що число {n} є простим, це {prime}" )
    if prime:
        print(n)

# ще щось робити з простими числами

