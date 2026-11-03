# Find & print the sum of the Fibonacci series upto n terms

n = int(input("Enter the number of terms: "))

a = 0
b = 1
total = 0
i = 1

while i <= n:
    total += a
    a, b = b, a + b
    i += 1

print("Sum of Fibonacci series:", total)
