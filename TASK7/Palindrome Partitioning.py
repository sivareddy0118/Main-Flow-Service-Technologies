# Program for Palindrome Partitioning

def is_palindrome(s):
    return s == s[::-1]

def partition(s):
    result = []
    def backtrack(start, path):
        if start == len(s):
            result.append(path)
            return
        for end in range(start + 1, len(s) + 1):
            if is_palindrome(s[start:end]):
                backtrack(end, path + [s[start:end]])
    backtrack(0, [])
    return result

text = "aab"
print("String:", text)
print("Palindrome Partitions:", partition(text))
