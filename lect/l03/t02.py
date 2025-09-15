n = int(input("n=? "))

# 1 + 2 + 3 + 4 + ... + i > n
# n = 10
# 1 + 2 + 3 + 4 + 5 > 10

s = 0
i = 1
while s <= n:
    print(f"{s=}, {i=}")
    s += i
    i += 1

print(s)
