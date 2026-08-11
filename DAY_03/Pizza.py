print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M or L? ")
pep = input("Do you want pepperoni? Y/N? ")
cheese = input("Do you want some extra cheese? Y/N? ")

bill = 0

if cheese == 'Y':
    bill += 1
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25
if pep == 'Y' and size == 'S':
    bill += 2
elif pep == 'Y':
    bill += 3

print(f"The pizza will be ${bill}.")