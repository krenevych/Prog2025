class Polynom:
    def __init__(self, coefs):
        self.coefs = coefs

    def __str__(self):
        return str(self.coefs)

    def __call__(self, x):
        res = 0
        for pow, coef in self.coefs.items():
            res += coef * x**pow
        return res

if __name__ == '__main__':
    P = Polynom({
        2:2,
        1:3,
        0:1
    })
    print(P)
    P_3 = P(3)
    print(P_3)

