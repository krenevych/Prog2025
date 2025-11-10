f = open("file1.txt")

for i in range(20):  # читання файлу 20 разів поспіль
    f.seek(0)  # !!! повертаємо маркер на початок
    print(f.read())

f.close()