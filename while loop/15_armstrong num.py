# Check whether the given num is an armstrong num

num = int(input("Enter number: "))

original = num

digits = 0

total = 0

#count the num of digits
temp = num
while temp > 0:
    digits += 1
    temp = temp // 10

#calculate the sum of digits raised to the power of num of digits
temp = num
while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == original:
    print("Number is an Armstrong number")
else:
    print("Number is not an Armstrong number")
