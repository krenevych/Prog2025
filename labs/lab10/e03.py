# 1 3 2
# 3 8 9
# 1 9 0

def read_matrix(N):
    M = []
    for i in range(N):
        row = [int(el) for el in input().split()]
        M.append(row)
    return M

def print_matrix(M, spaces=5):
    for i in range(len(M)):  # i пробігає індекси рядків
        for j in range(len(M[0])):
            print(f"{M[i][j]:{spaces}}", end="")
        print()
    # for row in M:
    #     print(row)


if __name__ == '__main__':
    N = int(input("Задайте кількість рядків матриці"))
    M = read_matrix(N)

    print_matrix(M, 10)