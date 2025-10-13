
my_string = "Hello,            world!"

words = my_string.split()

email3 = "KRENEVYCH@KNU.UA"

if "@" not in email3: # email3.count("@") == 1
    print("Заданий рядок не є електронною адресою")
else:
    splited_email = email3.split("@")
    pass