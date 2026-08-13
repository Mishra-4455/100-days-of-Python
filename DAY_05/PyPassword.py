import random
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input("Enter the number of letters: "))
num_numbers = int(input("Enter the number of numbers: "))
num_symbols = int(input("Enter the number of symbols: "))
S = []

for num in range(1, num_letters+1):
    S.append(random.choice(letters))
for num in range(1, num_numbers+1):
    S.append(random.choice(numbers))
for num in range(1, num_symbols+1):
    S.append(random.choice(symbols))

random.shuffle(S)
String = ""
for n in S:
    String += n

print(f"Your password is: {String}")