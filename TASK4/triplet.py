# Program to check if numbers form a Pythagorean triplet

a, b, c = 3, 4, 5
nums = sorted([a, b, c])

if nums[0]**2 + nums[1]**2 == nums[2]**2:
    print(a, b, c, "form a Pythagorean triplet")
else:
    print(a, b, c, "do not form a Pythagorean triplet")
