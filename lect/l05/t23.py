# Підрахувати кількість слів у введеному з клавіатури рядку

# s = "    hello    hello     word    "
s = input("Задайте рядок ")

# s_stripped = s.strip()

l_words = s.split()
print(len(l_words))
pass
