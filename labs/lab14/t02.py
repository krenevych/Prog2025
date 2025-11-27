s = "Boing 777"

suma = 0
for c in s:
    try:
        n = int(c)
        suma += n
    except ValueError:
        pass

print(suma)