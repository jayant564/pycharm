# Find and print the sum of all even numbers from 1 up to n

n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total = total + i

print(f"Sum of even numbers = {total}")
