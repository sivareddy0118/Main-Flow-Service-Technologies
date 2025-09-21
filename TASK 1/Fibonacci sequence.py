# Program to print Fibonacci sequence
n = int(input("Enter how many terms: "))
a, b = 0, 1
fib = []
for i in range(n):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci Sequence:", fib)
