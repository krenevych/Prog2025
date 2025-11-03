d = {1: "odin", 2: "dva", 3: "tri"}
print(d)

val = d.pop(1)  # у чому відмінність між del d[1]???
print(d)
print(val)

d.update([(3, 4), (5, 6)])
print(d)


