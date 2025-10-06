# зменшити всі елементи списку, що кратні трьом втричі

lst = [1, 12, 23, 18, 27] # => [1, 4, 23, 6, 9]

# for elem in lst:
#     if elem % 3 == 0: # якщо елемент ділиться на три
#         elem = elem // 3
#
#     print(elem, end=", ")

for i in range(len(lst)):
    if lst[i] % 3 == 0:
        lst[i] = lst[i] // 3

print()

print(*lst) # [1, 4, 23, 6, 9]