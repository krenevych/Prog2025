f = open("myfile.txt", "rt")  # 1 - відкриття файлу (текстового файлу "t" для читання "r"

# 2 - робота з інформацією, що стосується файлу
print("Content of the file:")
content = f.readline()
print(1, content)
content = f.readline()
print(2, content)

f.close()               # 3 - закриття файлу