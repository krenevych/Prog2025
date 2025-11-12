N = int(input())
elems = [int(e) for e in input().split()]
# 3 5 3 -7 7 5 -9 -4

freq = {} # частоти кожного числа
for el in elems:
    if el in freq:
        freq[el] += 1
    else:
        freq[el] = 1

result = []
for el in elems[::-1]:
    if freq[el] > 1 and el not in result:
        result.append(el)

if len(result) == 0:
    print("NO")
else:
    print(*result[::-1])