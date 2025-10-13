s = "45e6"

# print(s.isdigit())

isdigit = True
for ch in s:
    # перевірка чи є ch цифрою
    if not ("0" <= ch <= "9"):
        # якщо ні, то isdigit = False break
        isdigit = False
        break
    # print(f"{ch=}")

print(isdigit)
