# Сума чисел від 1 до 9
suma = 0
for i in range(10):
    # print(i, end=", ") # кожна операція print завершується не переводом курсора на наступний рядок, а символами, що вказані у параметрі end
    # print(i)
    suma += i # suma = suma + i

# print()
print("suma = ", suma)