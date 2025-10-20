# Визначити цифру, що входить до запису натурального
# числа найбільшу кількість разів та кількість її входжень.

# 334444132413211
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#  0  1  2  3  4  5  6  7  8  9

def frequency(n: int) -> list:  # ": int" означає, що при виклику буде очікуватися цілий тип, "-> list" означає, що від функції очікується, що вона повертає список
    freq = [0] * 10

    while n > 0:
        d = n % 10
        freq[d] += 1
        n = n // 10

    return freq

def max_el(array: list) -> tuple: # функція буде повертати кортеж з двох елементів - найбільший елемент списку, та його індекс
    max_i, max_elem = 0, array[0]

    for i, elem in enumerate(array):
    # for i, elem in enumerate(array[1:]): # !!!! вправа, зрозуміти, чому не правильно повертається індекс
        if elem > max_elem:
            max_i, max_elem = i, elem

    return max_elem, max_i

#### MAIN ####

# відлагоджування підпрограм
# print(frequency(3344556666))  # [0, 0, 0, 2, 2, 2, 4, 0, 0, 0]
# print(frequency(33444413200413211))  # [2, 4, 2, 4, 5, 0, 0, 0, 0, 0]
# frequency("2323")

f = frequency(33444413200413211)
freq_digit, max_digit = max_el(f)

print(max_digit)




