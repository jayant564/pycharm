# Calculate & print the factorial of every num from 1 to n

n = int(input("Enter number: "))

facto = 1

for i in range(1, (n+1)):
    facto *= i
    print(f"Factorial of {i} = {facto}")
