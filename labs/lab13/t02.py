with open("input02a.txt") as f:
    content = f.read()
    numbers =[float(n) for n in content.split()]
    print(numbers)
    print(sum(numbers))