n = int(input())

# digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
digits = [0] * 10

while n > 0:
    d = n % 10

    digits[d] += 1

    n = n//10

print(*digits)
