class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x}, {self.y}"

    def length2(self):
        return self.x ** 2 + self.y ** 2

    def length(self):
        return self.length2() ** 0.5

# class Vector3d:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"
#
#     def length2(self):
#         return self.x ** 2 + self.y ** 2 + self.z ** 2
#
#     def length(self):
#         return self.length2() ** 0.5

class Vector3d(Vector2D):
    def __init__(self, x, y, z):
            super().__init__(x, y)
            # Vector2D.__init__(self, x, y)
            self.z = z

    def __str__(self):
        # return f"{self.x}, {self.y}, {self.z}"
        return f"{super().__str__()}, {self.z}"

    def length2(self):
        return super().length2() + self.z ** 2


if __name__ == '__main__':
    v = Vector2D(3, 4)
    print(f"Vector2d: {v}")
    print(v.length())

    v3 = Vector3d(3, 4, 5)
    print(v3)
    print(v3.length())


