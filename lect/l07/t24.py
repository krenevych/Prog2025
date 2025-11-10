M = {2, 4, 8}
N = frozenset({4, 8, 16})

print(f"M | N : {M | N}")  # {16, 2, 4, 8}
print(f"N | M : {N | M}")  # frozenset({16, 2, 4, 8})

# d1 = 3 + 3.25  # float
# d2 = 3 + 3     # int

N1 = N - {16}
print(f"{N1=}")

N2 = set(N1)
print(f"{N2=}")
N2.discard(4)

print()
print(f"{N1=}")
print(f"{N2=}")



