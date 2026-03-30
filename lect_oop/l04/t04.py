class Program:
    def __init__(self, name: str):
        self.name = name

    def installation(self):
        print(f"installation of program {self.name}")

    def run(self):
        print(f"program {self.name} is running...")

class Mouse:
    def __init__(self):
        self.name = "Mouse"

class Keyboard:
    def __init__(self):
        self.name = "Keyboard"


class Computer:
    def __init__(self):
        self.installed_programs: list[Program] = []
        self.mouse = Mouse() # створення мишки разом з компʼютером
        self.keyboard = Keyboard() # створення клавіатури разом з компʼютером

    def install(self, program: Program):
        self.installed_programs.append(program)
        program.installation()

    def uninstall(self, program: Program):
        self.installed_programs.pop(program)

    def run_programs(self):
        for prog in self.installed_programs:
            prog.run()

if __name__ == '__main__':
    word = Program("Word")
    pycharm = Program("PyCharm")

    c = Computer()

    c.install(word)
    c.install(pycharm)

    c.run_programs()