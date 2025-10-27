# 1 1 2 3 5 8 13 ...
import time


def F(n):
    if n == 1:
        return 1
    elif  n == 0:
        return 1
    else:
        return F(n - 1) + F(n - 2)

def F_non_rec(n):
    f1, f2 = 1, 1
    for i in range(2, n+1):
        f1, f2 = f1 + f2, f1
    return f1

# MAIN

start = time.time()
print(F(30))
end = time.time()
print(f"Час виконання: {end - start:.4f} секунд")

start = time.time()
print(F_non_rec(100))
end = time.time()
print(f"Час виконання: {end - start:.4f} секунд")


