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

    def __len__(self):
        return 2

    def __setitem__(self, key, value):
        if key == 'x' or key == 0:
            self.x = value
        elif key == 'y' or key == 1:
            self.y = value

    def __getitem__(self, key):
        if key == 'x' or key == 0:
            return self.x
        elif key == 'y' or key == 1:
            return self.y
        raise KeyError("Помилка ключа")


if __name__ == '__main__':
    v = Vector(3, 4)
    print(len(v))
    v[0] = 5
    v['y'] = 6
    print(v)

    print(v["x"])
    print(v[1])
    # print(v[9])