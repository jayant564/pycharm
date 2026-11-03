# Reverse the given num & print the reversed value

num = int(input("Enter number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print(f"Reversed number = {reverse}")
