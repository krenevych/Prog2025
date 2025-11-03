
# my_dict = {"hello" : "world", 23: 45, "python": 3.14}
my_dict = {"hello" : "world", 23: 45, 23: 777, 55: "world", "python": 3.14}

my_list = [23, "world", 3.14]
#           0       1      2
print(my_list[1])  # виведення на екран першого (другого по порядку) елементу списка, тобто "world"

print(my_dict)

print(my_dict["hello"])
print(my_dict[23])

my_dict["hello"] = "WORLD!"
print(my_dict)