# перетворити велику латинську літеру у маленьку

distance = ord("a") - ord("A") # відстань між будь-якою великою літерою латинського алфавіту та відповідною їй маленькою літерою

# print(distance)

c_upper = input("задайте велику латинську літеру? ")

c_lower = chr(ord(c_upper) + distance)

print(c_lower)

pass