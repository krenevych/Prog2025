# s = "welcome to python"
s = input()
res = ""

for c in s:
    res = res + c

    if c in "aeiouy":
        res = res + c


print(res)