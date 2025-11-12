N = int(input())
N_2 = N // 2
elems = [int(e) for e in input().split()]

freq = {} # частоти кожного числа
for el in elems:
    if el in freq:
        freq[el] += 1
    else:
        freq[el] = 1

print(freq)
for d, count in freq:
    if count > N_2:
        print(d)
        break
else:
    print(-1)


