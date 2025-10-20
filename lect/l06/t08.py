def increment_list(a: list):
    a.append(1)

    print(f"{a=}")

########## MAIN ###########

my_list: list = [1, 1] # список - mutable
increment_list(my_list)

print(f"{my_list=}") # цо ми отримаємо на екрані??? my_list = [1, 1]
