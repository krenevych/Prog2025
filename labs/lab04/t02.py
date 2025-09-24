n = int(input())
#
# if n == 1:
#     print("Yes")
# elif n == 2:
#     print("Yes")

# Обчислити кiлькiсть двозначних чисел, цифри яких спадають.
# 32

# counter = 0
# for i in range(10, 100):
#     o = i % 10
#     d = i // 10
#
#     if d > o:
#         counter += 1

counter = 0
for d in range(1, 10):
    for o in range(0, 10):
        # print(d, o, sep="")
        if d > o:
            counter += 1

print(counter)