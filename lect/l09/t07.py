a = int(input("a="))

try:
    print(1 / a)
except ZeroDivisionError as err:
    print(err)