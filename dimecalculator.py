print("Welcome to THE CALCULATOR OD DIME")
print("What would you like 1.Addition(+), 2.Subtraction(-), 3.Multiplication(*), 4.Division(/)")
operation = input("Enter the operation you want to perform: ")
if operation not in ['+', '-', '*', '/']:
    print("Invalid operation. Please enter one of +, -, *, /.")
else:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        num1=int(num1)
        num2=int(num2)
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero.")
            result = num1 / num2
        print(f"The result of operation:", num1,operation,num2, "is:", result)
