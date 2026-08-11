print("Welcome to the Love Calculator!")
str1 = input("Enter your name? ")
str2 = input("Enter their name? ")
string = str1+str2

t = string.count("t")
r = string.count("r")
u = string.count("u")
e = string.count("e")

l = string.count("l")
o = string.count("o")
v = string.count("v")

side1 = str(t+r+u+e)
side2 = str(l+o+v+e)

num = int(side1 + side2)

if num < 10 or num > 90:
    print(f"Your score is {num}, you go together like coke and mentos.")
elif num >= 40 and num <= 50:
    print(f"Your score is {num}, you are alright together.")
else:
    print(f"Your score is {num}.")