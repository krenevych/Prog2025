# Обчислити кількість входжень символа a у рядок s

# S = input("Введіть рядок ")
# c = input("Задайте символ")

S = "hello world"
c = "l"

counter = 0
for ch in S:
    # print(ch)  # ch - отримує по одному символу з рядка у порядку розташування символів у рядку
    if ch == c:
        counter += 1

print(counter)
