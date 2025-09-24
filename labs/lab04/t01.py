# Дано натуральне число n.
# Вивести в порядку зростання n перших квадратів натуральних чисел.

n = int(input())

# for i in range(n):
#     # print(i)
#     print((i+1)**2, end=" ")

for i in range(1, n+1):
    print(i**2, end=' ')
