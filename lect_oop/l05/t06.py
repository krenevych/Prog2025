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
        elif isinstance(other, (tuple, list)) and len(other) == 2:
            return Vector(self.x + other[0], self.y + other[1])
        else:
            raise ArithmeticError("Правий операнд є несумнісного типу")

    def __imul__(self, other):
        if isinstance(other, (int, float)):
            self.x *= other
            self.y *= other
            return self
        elif isinstance(other, (tuple, list)) and len(other) == 2:
            self.x *= other[0]
            self.y *= other[1]
            return self
        elif isinstance(other, Vector):
            self.x *= other.x
            self.y *= other.y
            return self

    def __neg__(self):
        return Vector(-self.x, -self.y)


if __name__ == '__main__':
    v1 = Vector(1, 2)
    print(v1)

    # v1 += (2, 4 ) # v1 = v1 + 2
    # print(v1)

    v1 *= Vector(3, 4)
    print(v1)

    v2 = -v1
    print(v2)


