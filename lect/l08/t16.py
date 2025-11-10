import pickle

f = open("save_set", "rb")

M = pickle.load(f)
print(M)

f.close()