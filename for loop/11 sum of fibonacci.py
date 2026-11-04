# Find and print the sum of the Fibonacci series

n = int(input("Enter number of terms: "))

a = 0
b = 1
total = 0

for i in range(n):
    print(a, end=" ")
    total = total + a
    c = a + b
    a = b
    b = c

print("\nSum of Fibonacci series =", total)
