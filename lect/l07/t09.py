d = {1: "odin", 2: "dva", 3: "tri"}

# print(d[555]) # помилка
print(d.get(555))
print(d.get(555, "щось пішло не так"))

# del d[2]
print(d.get(2, "щось пішло не так"))

print(d.keys())
print(d.values())
print(d.items())