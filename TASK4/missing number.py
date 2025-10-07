# Program to find the missing number in a list

numbers = [1, 2, 3, 5]  # Missing number is 4
n = len(numbers) + 1
expected_sum = n * (n + 1) // 2
actual_sum = sum(numbers)
missing_number = expected_sum - actual_sum

print("Given Numbers:", numbers)
print("Missing Number is:", missing_number)
