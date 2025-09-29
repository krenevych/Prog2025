lst = [42, 32, 11, 8, 99, 8, 8, 22]
#       0   1   2  3   4  5  6   7

# print(423 in lst)
# print(423 not in lst)
#
# print(len(lst))
#
# print(min(lst))
# print(max(lst))

if 8 in lst:
    print(lst.index(8))
    print(lst.count(8))
else:
    print("елемент не міститься у списку")