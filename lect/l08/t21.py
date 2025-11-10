
import os

files = os.listdir(path=".")
print(files)

python_files = []
for path in files:
    name, ext = os.path.splitext(path)
    # print(os.path.splitext(path))
    if ext.lower() == ".py":
        python_files.append(path)

print(python_files)