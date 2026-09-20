print("Welcome to THE BME CALCULATOR")
name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
if gender == "male":
    print("nice to meet you Mr.", name)
elif gender == "female":
    print("nice to meet you Ms.", name)
else:
    print("Error, There is no gender like this. You are confused")  ##Stop the program here/
weight = input("Enter your weight in kg: ")
height = input("Enter your height in cm: ")
age = int(age)
weight = float(weight)
height = float(height)
BMI = weight / ((height / 100)**2)
print(f"Your BMI is:", BMI)
if BMI < 18.5:
    print("You are underweight.")
elif 18.5 <= BMI < 24.9:
    print("You have a normal weight.")
elif 25 <= BMI < 29.9:
    print("You are overweight.")
elif 30 <= BMI:
    print("Why are you increasing luggage on earth")    
elif BMI < 16:
    print("You are nothing but a skeleton. Just a air on earth")
else:
    print("Invalid BMI value. Please check your inputs.")
print("THANK YOU FOR USING THE BME CALCULATOR")