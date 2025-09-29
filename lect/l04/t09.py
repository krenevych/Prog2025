lst = [42, 32, 11, 8, 99, 4, 8, 22]
#       0   1   2  3   4  5  6   7  8

print(lst)

# new_lst = lst[1:6:1]
new_lst = lst[1:6]  # якщо крок 1, то :1 можна опустити
print(new_lst)

new_lst = lst[2: ]  # з другого елементу і до кінця списку з кроком 1
print(new_lst)

new_lst = lst[2: :2]  # з другого елементу і до кінця списку з кроком 2
print(new_lst)

new_lst = lst[::2]  # з нульового елементу до останнього з кроком 2
print(new_lst)

new_lst = lst[:]  # повна копія списку
print(new_lst)

new_lst = lst[2:]  # до кінця списку
print(new_lst)

