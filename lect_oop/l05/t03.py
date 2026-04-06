class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector: ({self.x}, {self.y})"
        # return f"{Vector.__name__}: ({self.x}, {self.y})"

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

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __complex__(self):
        return complex(self.x, self.y)

    def __float__(self):
        return float(self.x)


if __name__ == '__main__':
    v1 = Vector(3, 4)
    print(abs(v1))

    v1_str = str(v1)
    print(v1_str)

    c = complex(v1)
    print(c)

    v_x = float(v1)
    print(v_x)

    # n = int(input("Введіть ціле число"))