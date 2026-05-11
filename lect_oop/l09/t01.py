# абстрактний клас
class Pet:
    def __init__(self, name):
        self.name = name

    # абстрактний метод
    def voice(self):
        pass

if __name__ == '__main__':
    p = Pet("Pet") # пошушення - нам вдається створити екземпляр цього класу
    p.voice()  # викликаємо абстрактний метод