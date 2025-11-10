f = open("file1.txt")

print("позиція у файлі:", f.tell())
content = f.read(10)
print(content)
print("позиція у файлі:", f.tell())

f.seek(0)  # повертаємося на початок файлу
content = f.read()
print(content)

f.close()