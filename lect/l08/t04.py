f = open("file1.txt")  # 1 - відкриття файлу (текстового файлу "t" для читання "r"

content = f.read()
print(content)

# some code

print("Read file one more time:")

content = f.read()  #  змінна content буде містити порожній рядок, оскільки маркер лишився в кінці файлу після останньої операції читання
print(content)



print("END")

f.close()               # 3 - закриття файлу

# one more try
print("third attempt")
f = open("file1.txt")  # маркер знову стоїть на початку файлу
content = f.read()
print(content)
f.close()
print("END")