
lst = [2, 3, 4, 5]


d = dict.fromkeys(lst) # ключі - елементи списку lst, всі значення None
print(d)

d = dict.fromkeys(lst, 0) #  ключі - елементи списку lst, всі значення 0
print(d)
