# Check whether the given num is a perfect num

num = int(input("Enter a number: "))

total = 0

i = 1

while i < num:
    if num % i == 0:
        total = total + i
    i += 1

if total == num:
    print("Perfect number")
else:
    print("Not a perfect number")
