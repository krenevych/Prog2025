class Program:
    def __init__(self, name: str):
        self.name = name

    def installation(self):
        print(f"installation of program {self.name}")

    def run(self):
        print(f"program {self.name} is running...")


class Computer:

    def __init__(self, mouse, keyboard):
        self.installed_programs: list[Program] = []
        self.mouse = mouse
        self.keyboard = keyboard

    def install(self, program: Program):
        self.installed_programs.append(program)
        program.installation()

    def run_programs(self):
        for prog in self.installed_programs:
            prog.run()

if __name__ == '__main__':
    c = Computer("mouse", "keyboard")

    c.install(Program("Word"))
    c.install(Program("PyCharm"))

    c.run_programs()