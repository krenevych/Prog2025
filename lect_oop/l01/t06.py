import copy


class MyClass:
    def __init__(self, *args):
        self.a = list(args)

    def __str__(self):
        return str(self.a)

obj = MyClass(1, 2, 3)
print(obj)

obj2 = copy.deepcopy(obj)
obj2.a.append(1000)

print(obj)
print(obj2)