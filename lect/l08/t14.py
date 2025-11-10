f = open("replace.txt")
content = f.read()
f.close()

content = content.replace("computer", "COMPUTER")

f = open("replace.txt", "wt")
print(content, file=f)
f.close()
