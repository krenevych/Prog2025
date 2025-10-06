
lst = [34, 12, 31, 145, 298, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#       0   1   2    3    4

# i = 0  # номер поточного елементу списку
# for elem in lst:
#     print(i, elem)
#     i+= 1

for i, elem in enumerate(lst):  # enumerate(lst) - віддає пари - індекс + елемент списку
    print(i, elem)