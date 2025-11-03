d = {'first': 1, 'second': 2, 'third': 3, 3: 3}

print("======= Обхід за ключами ==============")
for k in d:
    print(k)

print("======= Обхід за ключами ==============")
for k in d.keys():
    print(k)
    # print(k, d[k]) # ключ-значення

print("========= Обхід за значеннями ============")
for v in d.values():
    print(v)

print("========= Обхід за ключами та значеннями ============")
# for k in d:
#     v = d[k]
#     print(k, v) # ключ-значення

for k, v in d.items():
    print(k, v)  # ключ-значення