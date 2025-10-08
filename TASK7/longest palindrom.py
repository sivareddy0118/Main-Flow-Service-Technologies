# Program to find the longest palindromic substring

def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest

text = "babad"
print("String:", text)
print("Longest Palindromic Substring:", longest_palindrome(text))
