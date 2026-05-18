# Домішки

class MovableMixin:  # домішок, що має метод move
    def move(self):
        print(f"Transport {self.mark} moves")

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

class MovableCar(Automobile, MovableMixin):
    pass

class MovableBicycle(Bicycle, MovableMixin):
    pass

class MovableMotorcycle(Motorcycle, MovableMixin):
    pass

if __name__ == '__main__':
    bicycle = MovableBicycle("Україна")
    motorcycle = MovableMotorcycle("Honda")
    car = MovableCar("Toyota")

    bicycle.move()
    motorcycle.move()
    car.move()

    # клас можемо створити - бо технічно домішок не є абстрактним класом, а лише концептуально, тобто на рівні домовленостей
    # movableMoxin = MovableMixin()
    # movableMoxin.move()  # цей метод породить помилку, бо в нас відсутні поля, які необхідні для цього методу


