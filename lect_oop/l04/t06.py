class A:
    def __init__(self, data):
        self._data = data

class B(A):
    def __init__(self, data):
        super().__init__(data)

class C(A):
    def __init__(self, data):
        super().__init__(data)
        self._data = "C changes data: " + self._data



class D(B, C):
    def __init__(self, data):
        A.__init__(self, data)
        B.__init__(self, data)

    def __str__(self):
        return f"{self._data}"

d = D("hello")
print(d)

print(D.__mro__)



