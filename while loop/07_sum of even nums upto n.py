# Calculate the sum of all even nums from 1 upto n

num = int(input("Enter number: "))

total = 0

while num > 0:
    if num % 2 == 0:
        total += num
    num -= 1

print(f"Sum of all even nums upto {num} = {total}")
