# Program to check if two strings are anagrams
str1 = "listen"
str2 = "silent"

if sorted(str1) == sorted(str2):
    print("Yes,", str1, "and", str2, "are anagrams.")
else:
    print("No,", str1, "and", str2, "are not anagrams.")
