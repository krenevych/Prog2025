# s = input()
s = "hello world"

freq = {c: s.count(c) for c in s}

print(freq)

freq_vowel = {c: s.count(c) for c in s if c in "ouyiea"}
print(freq_vowel)