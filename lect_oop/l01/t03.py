class NewClass:
    def __init__(self, par1, par2):
        self.p1 = par1
        self.p2 = par2

    def show(self):
        print(f"NewClass:{self.p1}, {self.p2}")

obj = NewClass("перший параметр", "другий параметр")

print(obj.p1)
obj.p1 = "змінений перший параметр"
print(obj.p1)

obj2 = NewClass("hello", "world")
print(obj2.p1)
print(obj2.p2)

obj.show()
obj2.show()

