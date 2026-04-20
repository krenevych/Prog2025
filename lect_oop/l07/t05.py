S = 1
N = int(input("N=? "))
for n in range(2, N+1):
    S = 2 * S + n * n

print(f"S({N})={S}")