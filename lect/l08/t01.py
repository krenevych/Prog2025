f = open("myfile.txt")  # 1 - відкриття файлу

# 2 - робота з інформацією, що стосується файлу
content = f.read()
print("Content of the file:")
print(content)

f.close()               # 3 - закриття файлу