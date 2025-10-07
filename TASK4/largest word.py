# Program to find the longest word in a sentence
sentence = "Mainflow Technologies provides internships"
words = sentence.split()
longest = max(words, key=len)

print("Sentence:", sentence)
print("Longest Word:", longest)
