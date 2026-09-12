fruits = ["Apple", "Pear", "Orange"]

#TODO: catch an exception and make sure the code executes
def make_pie(index):
    fruit = fruits[index]
    print(fruit,"pie")

try:
    make_pie(4)
except IndexError:
    print("The Fruit dosent exist.")