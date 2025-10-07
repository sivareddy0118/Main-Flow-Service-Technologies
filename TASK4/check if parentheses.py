# Program to check if parentheses are balanced

def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

expr = "{[()()]}"
print("Expression:", expr)
print("Balanced?" , is_balanced(expr))
