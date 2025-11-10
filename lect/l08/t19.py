import os

file_name = "replace1.txt"
if os.path.exists(file_name):
    f = open(file_name)
    content = f.read()
    f.close()

    print(content)


