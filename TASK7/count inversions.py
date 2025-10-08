# Program to count inversions in an array

def count_inversions(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

numbers = [2, 4, 1, 3, 5]
print("Array:", numbers)
print("Number of Inversions:", count_inversions(numbers))
