s = "+5-2+4-m/n*2:4"
# s = input()

res = 0 #

for c in s[1:]:
    if c in "+-*":     #c in ["+", "-", "*"]
        res += 1

print(res)