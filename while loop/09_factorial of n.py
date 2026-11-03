# Calculate & print the factorial of a given num

num = int(input("Enter number: "))

facto = 1

while num > 0:
    facto *= num
    num -= 1

print(f"Factorial of {num} = {facto}")
