
wallet = {
    10: 4,
    100: 1,
    2: 98,
    500: 10
}

max_value = 1000

suma = 0
for value in range(1, max_value+1):
    try:
        suma += wallet[value] * value
    except KeyError:
        pass

print(suma)

