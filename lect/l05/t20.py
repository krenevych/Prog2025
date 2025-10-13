email1 = "krenevych@knu.ua"
email2 = "KRENEVYCH@knu.ua"
email3 = "KRENEVYCH@KNU.UA"

email1_lower = email1.lower()
email2_lower = email2.lower()
email3_lower = email3.lower()

if email1_lower == email2_lower == email3_lower:
    print("одна й та ж електронна адреса")
else:
    print("адреси не збігаються")
