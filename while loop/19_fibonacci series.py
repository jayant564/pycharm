# Print the fibonacci series upto n terms

n = int(input("Enter the number of terms: "))

a = 0
b = 1
i = 1

while i <= n:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
