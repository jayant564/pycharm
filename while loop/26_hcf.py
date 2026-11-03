# Find the HCF of the two given nums

a = int(input("Enter 1 number: "))
b = int(input("Enter 2 number: "))

hcf = 0

i = 1

while i <= a and i <= b:
    if a % i == 0 and b % i == 0:
        hcf = i
    i += 1

print(f"HCF: {hcf}")
