class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            raise ArithmeticError("Правий операнд є несумнісного типу")

    def add(self, other):
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y
            )
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        else:
            raise ArithmeticError("Правий операнд є несумнісного типу")

if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1)
    print(v2)

    # v3 = v1.add(v2)      # v3 = v1 + v2
    v3 = v1 + v2
    # v3 = v1.__add__(v2)   # v3 = v1 + v2
    print(v3)
    #
    # v4 = v3 + 5
    # print(v4)
    #
    # v5 = Vector(5, 6) + "Hello"
    # print(v5)