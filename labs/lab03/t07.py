# n      reversed     d
# 124       0
# 12        4          4
# 1         42         2
# 0         421        1

n = int(input())
origin_n = n
reversed = 0
while n > 0:
    d = n % 10
    reversed = reversed * 10 + d
    n = n // 10

print(reversed)

if origin_n == reversed:
    print("Yes")
else:
    print("No")