from labs.lab13.t04_ import read_matrix, mult_matrix, write_matrix

M1 = read_matrix("m1.txt")
M2 = read_matrix("m2.txt")
try:
    # M_sum = add_matrix(M1, M2)
    M_mult = mult_matrix(M1, M2)
    # write_matrix(M_sum, "sum.txt")
    write_matrix(M_mult, "mult.txt")
except TypeError:
    print("Принаймні одна з матриць порожня, мабуть файлу, що містить матрицю не існує")
except AssertionError:
    print("Матриці перемножити не можна, бо кількість стовпчиків лівої матриці не збігається з кількістю рядків правої")