n = input()

# digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
digits = [0] * 10

for c in n:
    int_c = int(c)
    digits[int_c] += 1

print(*digits)
