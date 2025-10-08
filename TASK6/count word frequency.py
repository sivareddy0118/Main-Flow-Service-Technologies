# Program to count word frequency in a text

text = "Python internship at Mainflow teaches Python programming"
words = text.lower().split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:", word_count)
