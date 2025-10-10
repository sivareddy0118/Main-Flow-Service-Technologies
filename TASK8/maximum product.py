# Program to find maximum product subarray

def max_product(nums):
    max_prod = min_prod = result = nums[0]
    for n in nums[1:]:
        if n < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(n, max_prod * n)
        min_prod = min(n, min_prod * n)
        result = max(result, max_prod)
    return result

arr = [2, 3, -2, 4]
print("Array:", arr)
print("Maximum Product Subarray:", max_product(arr))
