# Program to convert decimal number to binary

num = 10
binary = ""
n = num

while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("Decimal:", num)
print("Binary:", binary)
