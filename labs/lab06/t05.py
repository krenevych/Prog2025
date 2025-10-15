# s = input()
s =     "WWWellcccooomee  ttoo PPyythooonn!!!"

res = s[0]


for c in s[1:]:
    if c != res[-1]:
        res += c

print(res)
