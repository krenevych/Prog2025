n = int(input())

if n == 0:
    print(1)
else:

    counter = 0
    while n > 0:
        # print(n)
        counter += 1
        n = n // 10

    print(counter)