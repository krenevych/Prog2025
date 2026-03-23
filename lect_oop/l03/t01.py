class Pet:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Pet {self.name}")

    ### багато різних методів для домашньої тваринки

    def eat(self):
        print(f"{self.name} eats something")


# Нам підходить все у класі Pet, але ми хочемо уточнити, що саме їсть тваринка
# нам не вистачає методу як тваринка говорить,
# наприклад, ми хочемо мати уточнення до класу Pet, а саме - Кіт
# Кіт їсть мишей та віскас, та каже "Няв"

class Cat(Pet):
    pass
    def eat(self):
        print(f"Cat {self.name} eats mice and Wiskas")

    def voice(self):
        print(f"Cat {self.name} says Miu-miu!")

p = Pet("Pet")
p.show()
p.eat()


c = Cat("Kuzya")
c.eat()
c.show()
c.voice()


