# Find & print the product of all digits of a given num

num = int(input("Enter number: "))

product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print(f"Product of digits: {product}")
