# Calculate & print the sum of first n natural num

num = int(input("Enter number: "))

total = 0

while num > 0:
    total += num
    num-=1

print(f"The sum of first {num} natural number = {total}")
