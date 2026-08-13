n = int(input("Enter the number till which you want to add:"))
sum = 0

for number in range(0, n, 2):
    sum += number
print(f"The sum of the all the even numbers from 1 to {n}, including 1 is {sum}.")