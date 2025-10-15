s = "PROGRAMMING CONTEST"
# s = input()

res = 0 #

for c in s:
    if c in "AEIOUY":
        res += 1

print(res)