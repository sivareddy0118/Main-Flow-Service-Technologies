# Program to find all permutations of a string

from itertools import permutations

text = "abc"
perm_list = [''.join(p) for p in permutations(text)]

print("String:", text)
print("All Permutations:", perm_list)
