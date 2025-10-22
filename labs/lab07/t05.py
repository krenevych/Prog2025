def bin_to_dec(b: str) -> int:
    res = 0
    pow = 1  # 1, 2, 4, 8, 16
    for d in b[::-1]:
        res = res + pow * int(d)
        pow *= 2

    return res


def dec_to_bin(n: int) -> str:
    if n == 0:
        return "0"

    res = ""

    while n > 0:
        d = n % 2
        res = str(d) + res
        n = n // 2

    return res


####### MAIN ###########

A = input()
B = input()

a_dec = bin_to_dec(A)
b_dec = bin_to_dec(B)

res = a_dec + b_dec

res_bin = dec_to_bin(res)
print(res_bin)
