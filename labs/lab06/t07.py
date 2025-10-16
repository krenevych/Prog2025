total_words_list = []
while True:
    try:
        words = input().split()
        total_words_list.extend(words)
        if len(words) == 0:
            break
    except:
        break


# print(total_words_list)

lens = [len(word) for word in total_words_list]

print(*lens)