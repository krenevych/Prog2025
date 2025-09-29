from h5py.h5t import convert

# d = 256

# d = 256  # число записане у десятковій системі числення
d = 174  # число записане у десятковій системі числення

# напишемо алгоритм, що перетворює це число з десяткової системи числення у десяткову

base = 8  # основа системи числення
new_base = 10 # основа числення, у яку ми перетворюємо

pow_base = 1
converted = 0
while d > 0:
    k = d % base
    # print(k, end="")
    d = d // base

    # converted = converted + k # сума цифр
    converted = k * pow_base + converted # сума цифр
    # print(converted)
    # print(pow_base)
    pow_base *= new_base

print(converted)


