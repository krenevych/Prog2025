res = 0

f = open("input.txt")

nums = [float(line) for line in f.readlines()]


f.close()

print("сума чисел у файлі буде", sum(nums))