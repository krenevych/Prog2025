N = int(input("Задайте N "))

f = open("out.txt", "wt") # відкриваємо текстовий файл для запису wt

for n in range(1, N + 1):
    print(n ** 2, file=f)
    # f.write(str(n**2) + "\n")
f.close()