# Program to find the median of two sorted arrays

a = [1, 3, 5]
b = [2, 4, 6]
merged = sorted(a + b)
n = len(merged)

if n % 2 == 0:
    median = (merged[n//2 - 1] + merged[n//2]) / 2
else:
    median = merged[n//2]

print("Merged Array:", merged)
print("Median:", median)
