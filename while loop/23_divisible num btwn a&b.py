# Print all nums btwn a and b that are divisible by 7

a = int(input("Enter 1 number: "))
b = int(input("Enter 2 number: "))

while a <= b:
    if a % 7 == 0:
        print(a, end=' ')
    a += 1
