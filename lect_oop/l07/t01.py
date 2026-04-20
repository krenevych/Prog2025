from math import sin, pi, exp

print(sin(pi / 3))
x = pi / 3
sin_pi_3 = x - x**3 / (2 * 3) + x**5 / (2 * 3 * 4 * 5) - x**7 / (2 * 3 * 4 * 5 * 6 * 7) + x ** 9 / (2 * 3 * 4 * 5 * 6 * 7 * 8 * 9)
print(sin_pi_3)

print(exp(3))
print(3.5 ** 3.4)
print(3.5 ** 3)
print(9 ** 0.5)