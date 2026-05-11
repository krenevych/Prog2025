from lect_oop.l09.t03 import Pet


class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def voice(self):
        print(f"Cat {self.name}: miu-miu...")

if __name__ == '__main__':
    cat = Cat("Ben")
    cat.voice()