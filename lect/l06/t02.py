def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    return prime  # повернення результату у місце її виклику

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#
#     return True  # повернення результату у місце її виклику

# Дано список натуральних чисел.
# Визначити ті з них які є простими числами

# lst = [int(el) for el in input("Задайте список натуральних чисел ").split()]
lst = [45, 13, 7, 16, 113, 5]

for n in lst:
    if is_prime(n): # виклик підпрограми # якщо число n просте:
        print(n)

# чи буде сума елементів списку простим число

suma = sum(lst)
if is_prime(suma): # виклик підпрограми
    print(f"{suma} буде простим числом")


