# Program to find LCM and GCD of two numbers

a = 12
b = 18

# Finding GCD
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

# Finding LCM
lcm = (a * b) // gcd

print("Numbers:", a, "and", b)
print("GCD:", gcd)
print("LCM:", lcm)
