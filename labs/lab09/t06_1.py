# Чи можна з літер слова a скласти слово b,
# причому кожну літеру можна використати тільки один раз?

a = input()
b = input()

freq_a = {c: a.count(c) for c in a}
freq_b = {c: b.count(c) for c in b}

# print(freq_a)
# print(freq_b)

for c in freq_b:
    if c not in freq_a or freq_a[c] < freq_b[c]:
        print("No")
        break
else:
    print("Ok")

