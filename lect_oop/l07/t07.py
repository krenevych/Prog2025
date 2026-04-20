#      Fn_2
#             Fn_1
# 1     1      2  3  5  8


N = int(input("N=? "))
Fn_2 = 1
Fn_1 = 1


for n in range(2, N+1):
    Fn_2, Fn_1 = Fn_1, Fn_2 + Fn_1
    # print(Fn_1, Fn_2)

print(f"Fn({N})={Fn_1}")