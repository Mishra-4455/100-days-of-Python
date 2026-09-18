age : int
height : float
is_human : bool
name : str

# by adding the ":" at the end you can specify what will be the data type for the variable moving forward
# it will expect given data type at any point of the program i.e. dynamic typing cannot be used for them

def police_station(age: int) -> bool:
    if age >= 18:
        return True
    else:
        return False

# By adding " -> " to the fuction we can specify the return type of the given function
# if nay other data type is returned it will give an error
