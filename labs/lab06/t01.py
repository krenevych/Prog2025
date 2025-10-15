# s = "+5-2+4-m/n*2:4"
s = input()

res = s.count("+", 1)
res += s.count("-", 1)
res += s.count("*", 1)

print(res)