def C(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return C(n-1, k-1) + C(n-1, k)

# MAIN


for n in range(6):
    for k in range(n+1):
        print(C(n, k), end=" ")
    print()