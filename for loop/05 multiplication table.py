# Print the multiplication table of a given num

num = int(input("Enter number: "))

print(f"Multiplication table of {num}")

for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")
