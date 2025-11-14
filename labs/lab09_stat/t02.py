N = int(input())
elems = [int(el) for el in input().split()]

freq = {}  # число: скільки разів воно трапляється
for elem in elems:
    if elem not in freq:
        freq[elem] = 1
    else:
        freq[elem] += 1

# print(freq)

# for el in freq:  # цикл for для словника здійснюється по ключах
#     print(el)

major_exist = False
for k, v in freq.items():  # ітерування по парах (ключ: значення)
    if v > N // 2:
        print(k)
        major_exist = True
        break
    # else:
    #     print(-1)
    #     break

if not major_exist:
    print(-1)

# print(N)
# print(elems)