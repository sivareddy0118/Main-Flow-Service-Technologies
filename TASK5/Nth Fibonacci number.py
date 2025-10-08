# Program to find the Nth Fibonacci number using dynamic programming

n = 3
fib = [0, 1]

for i in range(2, n + 1):
    fib.append(fib[i - 1] + fib[i - 2])

print("Fibonacci Sequence:", fib)
print(f"The {n}th Fibonacci Number is:", fib[n])
