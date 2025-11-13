# 1 3 2
# 3 8 9
# 1 9 0

M = []
# r = input()
N = int(input("Задайте кількість рядків матриці"))
for i in range(N):
    row = [int(el) for el in input().split()]
    M.append(row)

print(M)