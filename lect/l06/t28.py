# 1 1 2 3 5 8 13 ...


def F(n):
    if n == 1:
        return 1
    elif  n == 0:
        return 1
    else:
        return F(n - 1) + F(n - 2)


# MAIN

print(F(5))