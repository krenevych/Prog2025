f = open("input01a.txt", "rt")

# print(f.readlines())
# print(*f.readlines())
for line in f:
    print(line, end="")

f.close()
