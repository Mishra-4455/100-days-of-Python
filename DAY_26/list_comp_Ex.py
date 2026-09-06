# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [(nums*nums) for nums in numbers]
# print(squared_numbers)

# even_numbers = [nums for nums in numbers if nums%2 == 0]
# print(even_numbers)

with open("file1.txt") as file:
    cont1 = file.readlines()
with open("file2.txt") as file:
    cont2 = file.readlines()

result = [int(num) for num in cont1 if num in cont2]

print(result)
