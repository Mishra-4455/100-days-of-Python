Std_heights = input("Input a list of student heights: ").split( )
for n in range(0, len(Std_heights)):
    Std_heights[n] = int(Std_heights[n])

length = 0
sum = 0

for n in Std_heights:
    length += 1
print(f"The number of elements in the list: {length}")
for n in range(0, length):
    sum += Std_heights[n]
print(f"The sum of the elements: {sum}")
avg = round(sum/length)
print(f"The average of the weights are: {avg}")