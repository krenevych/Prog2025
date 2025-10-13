# Перевірити, чи є рядок симетричним

# s = input("Введіть рядок: ")
s = "abcba"
#    01234

sym = True
for i in range(len(s) // 2 + 1):
    if s[i] != s[len(s) - i - 1]:
        # print("не симетричний")
        sym = False
        break
# else:
#     print("симетричний")

if sym:
    print("симетричний")
else:
    print("не симетричний")


