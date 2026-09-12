try:
    file = open("a_file.txt")
    a_dict = {"Key" : "Value"}
    print(a_dict["Key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something written")
except KeyError as message:
    print(f"The key {message} not found.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height>3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight/height ** 2
print(bmi)