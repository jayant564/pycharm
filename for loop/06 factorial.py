# Calculate & print the factorial of a given num

num = int(input("Enter number: "))

facto = 1

for i in range(1, (num+1)):
    facto *= i

print(f"Factorial of {num} = {facto}")
