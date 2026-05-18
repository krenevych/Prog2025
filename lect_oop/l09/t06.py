# якщо можемо виділити спільного предка

class Transport:
    def __init__(self, mark):
        self.mark = mark

    def move(self):
        print(f"Transport {self.mark} moves")

class Automobile(Transport):
    pass

    # інші методи для автомобіля

class Bicycle(Transport):
    pass

    # інші методи для велосипеда

class Motorcycle(Transport):
    pass

    # інші методи для мотоцикла

