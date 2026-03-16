class Foo:  # foo, bar, baz
    def __init__(self, bar):
        self._bar = bar

    def _private(self): # прихований метод, бо він починається з знаку нижнього підкреслення
        print("Я приватний метод")

    def public(self):
        print("Я публічний метод")

    def __very_private(self):
        print("Дуже приватний метод")

    def call_very_private(self):
        print("Виклик дуже приватного методу з публічного методу")
        self.__very_private()

# MAIN
if __name__ == '__main__':
    f = Foo("hello")
    # print(f.bar)
    # f.bar = "world"
    # print(f.bar)
    f.public()
    f._private()
    # f.__very_private()
    f.call_very_private()
    print("Зараз викликатимемо ззовні зовсім приватний метод")
    f._Foo__very_private()


