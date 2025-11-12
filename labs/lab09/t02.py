N = int(input())
N_2 = N // 2
elems = [int(el) for el in input().split()]

elems_set = set(elems)

for el in elems_set:
    counter = elems.count(el)
    if counter > N_2:
        print(el)
        break
else:
    print(-1)

# print(N)
# print(elems)
# print(elems_set)