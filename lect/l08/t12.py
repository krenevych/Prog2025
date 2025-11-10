res = 0

f = open("input02.txt")

nums = [float(line) for line in f.read().split()]
print(nums)

f.close()

print("сума чисел у файлі буде", sum(nums))