# 1 0 1 2 4 9
# N = 10
a = 189

u, v, w = 1, 0, 1
n = 2

# while n < N + 1:
while w < a:
    # print(u, v, w)
    n += 1
    u, v, w = v, w, u + 2 * v + w

print(w)
