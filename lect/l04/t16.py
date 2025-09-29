
a = [42, 32, 11, 8, 99]
b = a[:]   # b = a.copy()

b[2] = 777

print(a)
print(b)