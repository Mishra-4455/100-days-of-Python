def add(*args):
    return sum(args)
# print(add(10,10,10,10,10,10,40))



def calculate(n, **kwargs):
    '''Converts the input given into a accessable dictionary, with proper keywords thus
    being called "kw"args, so now if i wanna make a calculator then i can take an input
    with the "n" variable and another dictionary in the **kwargs then if a "multiply"
    keyword is passed we can catch it and multiply with the "multiply" value from the
    dictionary.'''

    print(kwargs)
    add = n + kwargs["add"]
    mult = n * kwargs["multiply"]
    print(add , mult)

# calculate(10, add= 10, multiply= 10)



# Here we are making a example class to explain how optional arguments in **kwargs works 
class Car:
    '''Here the Car class takes in optional arguments "make", "model", etc. If we leave the argument
    empty i.e. do not enter anything with that keyword its noted as empty and displays "none" and if
    we do give an input with that keyword it gets inputed in the object defined by the class.'''

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")

my_car = Car(make= "Nissan", model= "GT-R", color= "Black")
# print(my_car.seats)
