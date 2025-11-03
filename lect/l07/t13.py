# S = input()

S = "матан матан матан супер супер матан"

words = S.split()  # ['матан', 'матан', 'матан', 'супер', 'супер', 'матан']
# print(words)

word_freq = {} # словник слів(ключі) разом з їхньою кількістю входжень (значення)
for word in words:
    if word not in word_freq:
        word_freq[word] = words.count(word)
print(word_freq)

max_word, max_count = word_freq.popitem()
for word, count in word_freq.items():
    if count > max_count:
        max_word, max_count = word, count

# while len(word_freq) > 0:
#     word, count = word_freq.popitem()
#     if count > max_count:
#         max_word, max_count = word, count


print(max_word, max_count)