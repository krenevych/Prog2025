
lst = [42, 32, 11, 8, 99, 4, 8, 22]
#       0   1   2  3   4  5  6   7   8 (=len(lst))
#      -8  -7  -6 -5  -4 -3 -2  -1

new_lst = lst[5:1:-1] # міняю місцями початок і кінець :)
print(new_lst)

new_lst = lst[-3:-7:-1] # міняю місцями початок і кінець :)
print(new_lst)

reversed = lst[::-1]
print(lst)
print(reversed)

