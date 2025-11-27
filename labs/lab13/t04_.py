def read_matrix(file_name):
    try:
        M = []
        cols = -1
        with open(file_name) as f:
            for line in f:
                row = [int(el) for el in line.split()]
                if cols == -1: cols = len(row)
                else:
                    if len(row) != cols:
                        raise ValueError
                M.append(row)
        # якийсь код обробки, дуже довгий
        return M
    except FileNotFoundError:
        return None
    except ValueError:
        return None


def write_matrix(M, file_name, spaces=5):
    with open(file_name, "w") as f:
        for i in range(len(M)):  # i пробігає індекси рядків
            for j in range(len(M[0])):
                print(f"{M[i][j]:{spaces}}", end="", file=f)
            print(file=f)

def add_matrix(M1, M2):
    assert len(M1) == len(M2)
    assert len(M1[0]) == len(M2[0])
    n = len(M1)
    m = len(M1[0])

    M = []
    for i in range(n):
        row = []
        for j in range(m):
            a = M1[i][j] + M2[i][j]
            row.append(a)
        M.append(row)
    return M

def mult_matrix(M1, M2):
    assert len(M1[0]) == len(M2)

    n = len(M1)
    m = len(M2[0])

    M = []
    for i in range(n):
        row = []
        for j in range(m):
            a = 0
            for k in range(len(M2)):
                a += M1[i][k] * M2[k][j]
            row.append(a)
        M.append(row)
    return M

if __name__ == '__main__':
    M1 = read_matrix("m1.txt")
    M2 = read_matrix("m2.txt")
    # M_sum = add_matrix(M1, M2)
    M_mult = mult_matrix(M1, M2)
    # write_matrix(M_sum, "sum.txt")
    write_matrix(M_mult, "mult.txt")
