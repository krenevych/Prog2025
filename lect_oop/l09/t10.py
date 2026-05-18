# Домішки
from abc import ABC, abstractmethod

# interface
class Movable(ABC):  # домішок, що має метод move
    @abstractmethod
    def move(self): # задає поведінку
        pass

class Automobile:
    def __init__(self, mark):
        self.mark = mark

    # інші методи для автомобіля

class Bicycle:
    def __init__(self, mark):
        self.mark = mark

    # інші методи для велосипеда

class Motorcycle:
    def __init__(self, mark):
        self.mark = mark

    # інші методи для мотоцикла

class MovableCar(Automobile, Movable):
    def move(self):
        print(f"Transport {self.mark} moves")

class MovableBicycle(Bicycle, Movable):
    def move(self):
        print(f"Transport {self.mark} moves")

class MovableMotorcycle(Motorcycle, Movable):
    def move(self):
        print(f"Transport {self.mark} moves")

if __name__ == '__main__':
    bicycle = MovableBicycle("Україна")
    motorcycle = MovableMotorcycle("Honda")
    car = MovableCar("Toyota")

    bicycle.move()
    motorcycle.move()
    car.move()



