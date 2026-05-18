# Домішки

class MovableMixin:  # домішок, що має метод move
    def move(self):
        print(f"Transport {self.mark} moves")

class Automobile(MovableMixin):
    def __init__(self, mark):
        self.mark = mark

    # інші методи для автомобіля

class Bicycle(MovableMixin):
    def __init__(self, mark):
        self.mark = mark

    # інші методи для велосипеда

class Motorcycle(MovableMixin):
    def __init__(self, mark):
        self.mark = mark

    # інші методи для мотоцикла

if __name__ == '__main__':
    bicycle = Bicycle("Україна")
    motorcycle = Motorcycle("Honda")

    bicycle.move()
    motorcycle.move()

