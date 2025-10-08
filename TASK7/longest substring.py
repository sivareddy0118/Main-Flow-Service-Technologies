# Program to find longest substring without repeating characters

def longest_unique_substring(s):
    seen = {}
    start = max_len = 0
    for i, ch in enumerate(s):
        if ch in seen and seen[ch] >= start:
            start = seen[ch] + 1
        seen[ch] = i
        max_len = max(max_len, i - start + 1)
    return max_len

text = "abcabcbb"
print("String:", text)
print("Length of Longest Unique Substring:", longest_unique_substring(text))
