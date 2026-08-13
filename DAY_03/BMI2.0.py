weight = float(input("Enter your weight in Kg:"))
height = float(input("Enter your height in m:"))

BMI = weight/height ** 2
if BMI < 18.5:
    print(f"Your BMI is {round(BMI)}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {round(BMI)}, you are Healthy.")
elif BMI < 30:
    print(f"Your BMI is {round(BMI)}, you are overweight.")
elif BMI < 35:
    print(f"Your BMI is {round(BMI)}, you are obese.")
else:
    print(f"Your BMI is {round(BMI)}, you are clinically obese.")