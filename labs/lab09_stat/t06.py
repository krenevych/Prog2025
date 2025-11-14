a = input()  # abrakadabra
b = input()  # dakar

freq_a = {ch: a.count(ch) for ch in a}
freq_b = {ch: b.count(ch) for ch in b}
print(freq_a)
print(freq_b)

for ch, count in freq_b.items():
    if ch not in freq_a or freq_a[ch] < freq_b[ch]:
        print("No")
        break
else:
    print("Ok")

pass


