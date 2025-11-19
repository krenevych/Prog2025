with open("output03.txt", "wt") as f:
    for i in range(1, 10):
        print(str(i) * i, file=f) # file=f означає перенаправити вивід у файл а