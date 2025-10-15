s = "  Alexandr    Sergeevich   Pushkin   "
res = s[0]
# _Alexandr_

# res = " ".join(s.split())

for c in s[1:]:
    if c != " ":
        res += c
    else:
        if res[-1] != " ":
            res += " "

if res[-1] == " ":
    res = res[:-1]

if res[0] == " ":
    res = res[1:]

print(res)