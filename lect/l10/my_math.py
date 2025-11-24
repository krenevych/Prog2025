def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False

    return True  # повернення результату у місце її виклику


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

pi = 3.1415
e = 2.7

# for debug
if __name__ == "__main__":
    print("Hello from my_math")

    print(pi)
    print(e)

    print(factorial(10))
    print(factorial(0))
    print(is_prime(4))
    print(is_prime(13))
