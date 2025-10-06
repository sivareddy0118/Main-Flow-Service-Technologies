# Program to Sort a List in Ascending Order

data = [5, 2, 8, 1, 3]
for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]

print("Sorted List:", data)
