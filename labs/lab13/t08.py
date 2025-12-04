def read_polynom(file_name):
    polynom = {}
    try:
        with open(file_name) as f:
            for line in f:
                pow, coef = line.split()
                coef = float(coef)  # коефіцієнт дійсний
                pow = int(pow)  # степінь лише цілий
                if pow in polynom: # якщо коефіцієнт при такому степені вже є в словнику
                    polynom[pow] += coef
                else:  # коефіцієнт при такому степені трапляється впеше
                    polynom[pow] = coef
    except FileNotFoundError:
        return None
    except ValueError:
        return None

    return polynom

# def print_polynom(poly: dict):
#     keys = list(poly.keys())
#     keys.sort()
#     keys = keys[::-1]
#     poly_str = ""
#     for key in keys:
#         if key == 1:
#             poly_str += f"{poly[key]}x + "
#         elif key == 0:
#             poly_str += f"{poly[key]} + "
#         else:
#             poly_str += f"{poly[key]}x^{key} + "
#
#     print(poly_str[:-3])

def print_polynom(poly: dict, file=None):
    keys = list(poly.keys())
    keys.sort()
    keys = keys[::-1]
    poly_list = []
    for key in keys:
        if key == 1:
            poly_list.append( f"{poly[key]}x")
        elif key == 0:
            poly_list.append( f"{poly[key]}")
        else:
            poly_list.append( f"{poly[key]}x^{key}")

    if file == None:
        print(*poly_list, sep=" + ")
    else:
        with open(file, "w") as f:
            print(*poly_list, sep=" + ", file=f)

def derivative(poly: dict):
    der = {}
    for pow, coef in poly.items():
        if pow == 0:
            continue

        der[pow - 1] = coef * pow

    return der

def suma(p1: dict, p2: dict):
    p = {}

    pows = set(p1.keys()) | set(p2.keys()) # set(p1) | set(p2)
    # print("==========")
    for pow in pows:
        coef1 = p1.get(pow, 0)  # якщо в словнику немає ключа pow, то отриємо 0
        coef2 = p2.get(pow, 0)
        # print(f"{coef1=}", f"{coef2=}")
        p[pow] = coef1 + coef2

    return p

def mult(poly1: dict, poly2: dict):
    p = {}

    for p1, c1 in poly1.items():
        for p2, c2 in poly2.items():
            result_p = p1 + p2
            result_c = c1 * c2
            if result_p not in p:
                p[result_p] = result_c
            else:
                p[result_p] += result_c

    return p

if __name__ == '__main__':
    p1 = read_polynom("t08_p1.txt")
    p2 = read_polynom("t08_p2.txt")

    # print(p1)
    print_polynom(p1)
    p_der = derivative(p1)
    print_polynom(p_der)
    # print_polynom(p1, "out_t08.txt")
    p_sum = suma(p1, p2)
    p_mult = mult(p1, p2)
    print_polynom(p_sum)
    print_polynom(p_mult)