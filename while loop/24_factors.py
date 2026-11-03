# Print all factors of the given num

num = int(input("Enter number: "))

i = 1

while i <= num:
    if num % i == 0:
        print(i, end=' ')
    i += 1
