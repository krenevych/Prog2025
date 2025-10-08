n = int(input())
lst = []

for i in range(n):
    elem = int(input())
    lst.append(elem)

# lst = lst[::-1] # тільки в Python

for i in range(n // 2):
    # lst[i] <-> lst[n-1-i]
    # a = lst[i]
    # lst[i] = lst[n-1-i]
    # lst[n-1-i] = a

    lst[i], lst[n - 1 - i] = lst[n - 1 - i], lst[i]

print(*lst)
