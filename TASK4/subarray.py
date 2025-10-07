# Program to find subarray with a given sum

arr = [1, 2, 3, 7, 5]
target_sum = 12
current_sum = 0
start = 0
found = False

for end in range(len(arr)):
    current_sum += arr[end]
    while current_sum > target_sum:
        current_sum -= arr[start]
        start += 1
    if current_sum == target_sum:
        print("Subarray with sum", target_sum, "is from index", start, "to", end)
        found = True
        break

if not found:
    print("No subarray found with sum", target_sum)
