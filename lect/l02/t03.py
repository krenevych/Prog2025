a = 100500

b = False

c = a and b  # 100500 and False

print(c)

c = 1 or False  # Вправа, почитати на сайті з документацією Python, чому операція or разом з цілими повертає ціле !!!
print(c)
pass

if c:
    print("Hello")