import random 

namesString = input("Enter your names seperated by commas, I will select who gives the bill.")
names = namesString.split(", ")

index = random.randint(0, len(names) -1)
print(f"{names[index]} will give the bill.")