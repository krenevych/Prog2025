lst = [12, 323, 53]
st  = {12, 323, 53}
st1  = {12, 323, 53}

print(42 not in lst)
print(42 not in st)
print(12 in lst)
print(12 in st)

st2 = {34, 12, 1}
print(st == st2)
print(st == st1)
print(  st == set(lst)  )  # перевірка чи складається множина та список з однакових елементів