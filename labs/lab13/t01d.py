# d)	пошуку найдовшого рядка;

with open("input01a.txt", "rt") as f:
    max_line = f.readline()
    for line in f:
        if len(line) > len(max_line):
            max_line = line


    print("MAX_LINE = ", max_line)
