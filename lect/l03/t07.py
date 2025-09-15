# Чи містить число цифру 2
n = int(input("n=? "))


contains2 = False

while n > 0:
    d = n % 10

    if d == 2:
        contains2 = True

    n = n // 10

print(contains2)