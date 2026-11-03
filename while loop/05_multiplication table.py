# Print the multiplication table of a given num from nx1 to nx10

num = int(input("Enter number: "))

i = 1

while i <= 10:
    print(f"{num} X {i} = {num*i}")
    i+=1
