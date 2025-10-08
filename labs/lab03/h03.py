n = input() # рядок

res = ""
for c in n:
    if int(c) % 2 == 0:
        res =  res + str(int(c) + 1)
    else:
        res = res + str(int(c) - 1)

print(int(res))
