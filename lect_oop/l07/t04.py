x = 2
an = 1 # an - поточний член послідовності
for n in range(1, 10):
    an *= x / n   # an = x / n * an

print(an) # an - 9й член послідовності