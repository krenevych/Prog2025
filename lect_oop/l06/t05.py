class FactorialGenerator:
    def __init__(self, n):
        self.n = n  # треба порахувати n!
        self.k = 0 # номер поточного
        self.factorial = 1 # 0!

    def __iter__(self):
        return self

    def __next__(self):
        if self.k == 0:
            self.k = 1
            return self.factorial
        if self.k <= self.n:
            self.factorial *= self.k
            self.k += 1
            return self.factorial
        else:
            raise StopIteration()


if __name__ == '__main__':
    # factGenerator = FactorialGenerator(10)
    for f in FactorialGenerator(5):
        print(f)