# res = max(2, 3, 3, 2, 5, 18)
# print(res)


def custom_max(*args):
    # *args - означає, що параметром функції є послідовність значень розділених комою, при цьому args є кортежем
    # print(args)
    res = args[0]
    for el in args[1:]:
        if el > res:
            res = el

    return res

####### MAIN ###########
m = custom_max(2)
print(m)