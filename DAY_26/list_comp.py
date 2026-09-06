# List comprihension
# The process of making it easier to manipulate Lists making it easier to read and short
# new_list = [new_item for item in list]

# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [2*n for n in range(0,3)]
# print(new_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]
print(short_names, long_names)