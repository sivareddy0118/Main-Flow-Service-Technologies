# Program to find duplicates in a list

numbers = [1, 2, 3, 2, 4, 5, 3, 6]
duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Original List:", numbers)
print("Duplicate Elements:", duplicates)
