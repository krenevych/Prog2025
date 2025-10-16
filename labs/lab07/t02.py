def prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False

    return True

def sqr(k):
    i = 1
    while i**2 <= k:
        if i**2 == k:
            return True
        i += 1

    return False

def pow5(k):
    while k > 1:
        if k % 5 != 0:
            return False
        k = k // 5

    return True


# print(pow5(125))
# print(pow5(625))
# print(pow5(100))
# print(pow5(131))

# print(sqr(9))
# print(sqr(7))
# print(sqr(123))
# print(sqr(625))

######### MAIN PROGRAM ###########

# n = int(input())
lst = [int(el) for el in input().split()]

primes = [] # прості числа
sqrs = [] # повні квадрати
powers = [] # степені 5

for el in lst:
    if prime(el):
        primes.append(el)

    if sqr(el):
        sqrs.append(el)

    if pow5(el):
        powers.append(el)

print("прості числа:", primes)
print("повні квадрати:", sqrs)
print("степені 5:", powers)

