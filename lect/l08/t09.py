f = open("file1.txt")

for line in f:
    line = line.rstrip()  # обрізаємо символи '\n' в кінці кожного рядка
    # print(line, end="")   # якщо не обрізаємо символи '\n', то вказуємо відповідний параметер функції print
    print(line)

f.close()