# Program to sort a list using Bubble Sort

numbers = [5, 2, 9, 1, 3]
print("Before Sorting:", numbers)

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("After Sorting:", numbers)
