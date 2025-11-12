S = input()

freq = {c: S.count(c) for c in S}

max_c = max(freq)
print(max_c, freq[max_c])
