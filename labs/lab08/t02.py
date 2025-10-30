def mult(n, m):
    if m == 0:
        return 0
    else:
        return n + mult(n, m - 1)

# MAIN

print(mult(10, 5))