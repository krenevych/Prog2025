lst = [1, 4, 9, 16]
#      0  1  2   3

print(lst[0])
print(lst[3])
# print(lst[4])  # помилка IndexError

lst[0] = 111

print(lst)  # [111, 4, 9, 16]
