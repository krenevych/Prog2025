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

if __name__ == '__main__':
    p1 = read_polynom("t08_p1.txt")
    # print(p1)
    print_polynom(p1)
    # print_polynom(p1, "out_t08.txt")