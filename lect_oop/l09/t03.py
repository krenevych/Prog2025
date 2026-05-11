from abc import abstractmethod, ABC


# абстрактний клас
class Pet(ABC):
    def __init__(self, name):
        self.name = name

    # абстрактний метод
    @abstractmethod
    def voice(self):
        pass

# нащадок абстрактного класу - конкретний клас
class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def voice(self):
        print(f"Dog {self.name}: bau-bau...")

if __name__ == '__main__':
    # p = Pet("Pet") # пошушення - нам вдається створити екземпляр цього класу
    # p.voice()  # викликаємо абстрактний метод
    d = Dog("Barbos")
    d.voice()
