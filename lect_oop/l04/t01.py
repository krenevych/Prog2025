class Program:
    def __init__(self, name: str):
        self.name = name

    def installation(self):
        print(f"installation of program {self.name}")


class Computer:

    def __init__(self):
        pass

    def install(self, program: Program):
        program.installation()

if __name__ == '__main__':
    c = Computer()
    p = Program("Word")

    c.install(p)