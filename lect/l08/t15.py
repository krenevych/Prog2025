import pickle

M = {2, 4, 8, 56, 18, "hello"}

f = open("save_set", "wb")

pickle.dump(M, f)

f.close()