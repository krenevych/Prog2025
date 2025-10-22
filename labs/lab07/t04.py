def gcd(a: int, b: int) -> int:
    if a < b:  # сортуємо змінні, так, щоб a > b
        a, b = b, a

    while b != 0:
        a, b = b, a % b

    return a

print(gcd(105, 385))