n = int(input())

if n == 1:
    print(4)
else:
    res = 45 * 10**(n-2)
    print(res)

# for n in range(1, 10):
#     start = 10 ** (n-1)
#     end = 10 ** n
#
#     # print(start, end)
#     counter = 0
#     for i in range(start, end):
#         if i % 2 == 0:
#             counter += 1
#
#     print(counter)