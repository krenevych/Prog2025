f = open("input.txt")

res = 0
for line in f:
    n = float(line)
    res += n

f.close()

print("сума чисел у файлі буде", res)