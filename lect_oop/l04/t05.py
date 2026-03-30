class XeroxBase:
    def copy(self):
        print("Xerox: copy")























class Xerox(XeroxBase):
    pass

class Scaner:
    def copy(self):
        print("Scaner: copy")


class MFD(Xerox, Scaner):
    def copy(self):
        Scaner.copy(self)

mfd = MFD()
mfd.copy()