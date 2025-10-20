def increment_int(a: int):
    a += 1

    print(f"{a=}")

######## MAIN #########

my_int: int = 10  # цілий тип - immutable
increment_int(my_int)  # a = my_int

print(f"{my_int=}") # що ми отримаємо на екрані??? my_int=11