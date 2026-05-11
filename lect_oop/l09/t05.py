from abc import ABC, abstractmethod


class Diagnosable(ABC):

    @abstractmethod
    def diagnose(self):
        pass

###############
class Student:
    def __init__(self, name):
        self.name = name
        self._health = 100

    def pass_exam(self):
        self._health -= 10
        if self._health < 0:
            self._health = 0

    def have_rest(self):
        self._health += 10
        if self._health > 100:
            self._health = 100

class Car:
    def __init__(self, resource = 100_000):
        self._resource = resource
        self._current_mileage = 0

    def drive(self):
        self._current_mileage += 10_000

    def pass_service(self):
        self._resource += 100_000

###############
class CarDiagnosable(Car, Diagnosable):
    def diagnose(self):
        if self._current_mileage >= self._resource:
            print("You have to pass service!")
        else:
            rest = self._resource - self._current_mileage
            rest /= self._resource
            rest *= 100
            print( f"rest {rest}% of resource")


class StudentDiagnosable(Student, Diagnosable):
    def diagnose(self):
        if self._health == 0:
            print("You have to rest!")
        else:
            print(f"{self._health}% health")


if __name__ == '__main__':
    car = CarDiagnosable()
    car.diagnose()
    car.drive()
    car.drive()
    car.drive()
    car.drive()
    car.diagnose()
    car.pass_service()
    car.diagnose()

    student = StudentDiagnosable("Ben")
    student.diagnose()
    student.pass_exam()
    student.pass_exam()
    student.pass_exam()
    student.pass_exam()
    student.pass_exam()
    student.diagnose()

    diagnosables: list[Diagnosable] = [
        CarDiagnosable(),
        student,
        car,
    ]

    def foo(some_list: list[Diagnosable]):
        print("=============")
        for d in some_list:
            d.diagnose()

    foo(diagnosables)

