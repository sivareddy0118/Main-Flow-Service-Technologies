# Program to generate all valid parentheses combinations

def generate_parentheses(n, open_count=0, close_count=0, current="", result=None):
    if result is None:
        result = []
    if len(current) == 2 * n:
        result.append(current)
        return result
    if open_count < n:
        generate_parentheses(n, open_count + 1, close_count, current + "(", result)
    if close_count < open_count:
        generate_parentheses(n, open_count, close_count + 1, current + ")", result)
    return result

n = 3
print("All Valid Parentheses Combinations:", generate_parentheses(n))
