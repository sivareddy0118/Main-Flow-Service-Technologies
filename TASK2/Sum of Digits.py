# Program to find the Sum of Digits of a number

num = 1234
total = 0
temp = num

while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10

print("Number:", num)
print("Sum of Digits:", total)
