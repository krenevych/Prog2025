def gcd(a: int, b: int) -> int:
    if a < b:  # сортуємо змінні, так, щоб a > b
        a, b = b, a

    while b != 0:
        c = a % b
        a = b
        b = c

    return a

print(gcd(105, 385))