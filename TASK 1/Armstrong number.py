# Program to check Armstrong number
num = int(input("Enter a number: "))
order = len(str(num))
sum_val = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_val += digit ** order
    temp //= 10

if num == sum_val:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
