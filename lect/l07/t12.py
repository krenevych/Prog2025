# S = input()

S = "матан матан матан супер супер матан"

words = S.split()  # ['матан', 'матан', 'матан', 'супер', 'супер', 'матан']
# print(words)

# Спосіб 1
word_freq = {word: words.count(word) for word in words}
print(word_freq)

# Спосіб 2
word_freq = {} # слоник слів(ключі) разом з їхньою кількістю входжень (значення)
for word in words:
    if word not in word_freq:
        word_freq[word] = words.count(word)
print(word_freq)

