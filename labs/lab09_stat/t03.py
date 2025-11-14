N = int(input())
elems = [int(el) for el in input().split()]

freq = {el: elems.count(el) for el in elems}

# print(freq)

for el in elems:
    if el in freq and freq[el] == 1:
        print(el, end=" ")