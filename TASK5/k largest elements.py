# Program to find K largest elements in a list

numbers = [10, 4, 3, 50, 23, 90]
k = 3
numbers.sort()

print("List:", numbers)
print(f"{k} Largest Elements:", numbers[-k:])
