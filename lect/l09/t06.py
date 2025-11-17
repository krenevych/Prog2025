
suma = 0

while True:
    try:
        a = input("Введіть ціле число ")
        if a == "стоп":
            break
        a = int(a)
        suma += a
    except ValueError:
        print("Введене вами значення, не є цілим числом")

print("Сума = ", suma)

