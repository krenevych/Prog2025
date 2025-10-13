my_string = "hello, hello world"
#            0123456789012

find_hello = my_string.find("hello")

print(find_hello)

find_hello2 = my_string.find("hello", 2)
index_hello2 = my_string.index("hello", 2)

print(find_hello2)
print(f"{index_hello2=}")

find_hello2_9 = my_string.find("hello", 2, 9)

print(find_hello2_9)

print(my_string.replace("hello", "HELLO"))