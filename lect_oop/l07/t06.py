       # Fn_2  Fn_1  Fn
# 2    #    1     1   2
# 3    #    1     2   3
# 4    #    2     3   5
# 5    #    3     5   8

N = int(input("N=? "))
Fn_2 = 1
Fn_1 = 1


for n in range(2, N+1):
    Fn = Fn_1 + Fn_2
    Fn_2 = Fn_1
    Fn_1 = Fn

print(f"Fn({N})={Fn_1}")