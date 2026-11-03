# Find & print the sum of all factors of the given num

num = int(input("Enter number: "))

total = 0

i = 1

while i <= num:
    if num % i == 0:
        print(i, end=' ')
        total += i
    i += 1

print()

print(f"Sum of all factors = {total}")
