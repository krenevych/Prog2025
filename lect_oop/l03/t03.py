from lect_oop.l03.t02_Pet import Pet, HunterDog, Cat

pet = Pet("Pet")
# p.eat()

hd = HunterDog("Guffie")
# hd.eat()

pets : list[Pet] = []
pets.append(pet)
pets.append(hd)
pets.append(Cat("Murchik"))

for p in pets:
    p.eat()