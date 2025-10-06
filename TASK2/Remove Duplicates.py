# Program to Remove Duplicates from a List

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for n in numbers:
    if n not in unique_list:
        unique_list.append(n)

print("Original List:", numbers)
print("List without Duplicates:", unique_list)
