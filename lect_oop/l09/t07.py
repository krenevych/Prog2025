# Якщо не можемо виділити

class Automobile:
    def __init__(self, mark):
        self.mark = mark

    def move(self):
        print(f"Transport {self.mark} moves")

    # інші методи для автомобіля

class Bicycle:
    def __init__(self, mark):
        self.mark = mark

    def move(self):
        print(f"Transport {self.mark} moves")

    # інші методи для велосипеда

class Motorcycle:
    def __init__(self, mark):
        self.mark = mark

    def move(self):
        print(f"Transport {self.mark} moves")

    # інші методи для мотоцикла

if __name__ == '__main__':
    bicycle = Bicycle("Україна")
    motorcycle = Motorcycle("Honda")

    bicycle.move()
    motorcycle.move()

