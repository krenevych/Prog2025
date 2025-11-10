import os
import shelve

# print(os.getcwd())

d = shelve.open("data")

# d["1"] = 15
# d["hello"] = "world"
# d["hello"] = "WORLD"

for k, v in d.items():
    print(k, v)

d.close()