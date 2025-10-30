def gcd(n, m):
    if m > n:
        return gcd(m, n)
    elif m != 0:
        return gcd(m, n % m)
    else:
        return n

# MAIN
print(gcd(5 * 7 * 9, 7 * 9 * 11))