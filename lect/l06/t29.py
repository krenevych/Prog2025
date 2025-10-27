# 0! = 1 - тривіальний (термінальний) випадок
# n! = (n-1)! * n, n >= 1

def fact(n):
    if n == 0:  # термінальна гілка
        return 1
    else:  # рекурсивна гілка
        return fact(n - 1) * n


def fact_non_req(n):
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res


# MAIN
print(fact(5))
print(fact_non_req(5))
