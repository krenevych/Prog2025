class Pet:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Pet {self.name}")

    ### багато різних методів для домашньої тваринки

    def eat(self):
        print(f"{self.name} eats something")

class Cat(Pet):
    def eat(self):
        print(f"Cat {self.name} eats mice and Wiskas")

    def voice(self):
        print(f"Cat {self.name} says Miu-miu!")

class Dog(Pet):
    def voice(self):
        print("Dog", self.name, "says:", "Bau - bau!!!")

class HunterDog(Dog):
    def eat(self):
        print(f"{self.name} eats luxury meal!!")

class Parrot(Pet):
    def voice(self):
        print("Parrot says:", self.name + " good boy!")


if __name__ == '__main__':

    p = Pet("Pet")
    p.show()
    p.eat()


    c = Cat("Kuzya")
    c.eat()
    c.show()
    c.voice()

    my_dog = Dog("Barbos")
    my_dog.voice()

    hd = HunterDog("Guffie")
    hd.eat()


