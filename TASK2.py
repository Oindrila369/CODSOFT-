#arithmetic operations
def calculate(num1, num2, operator):
    if (operator == '+'):
        return (num1 + num2)
    elif (operator == '-'):
        return (num1 - num2)
    elif (operator == '*'):
        return (num1 * num2)
    elif (operator == '/'):
        if (num2 == 0):
            return ("Cannot be divided by 0")
        return (num1 / num2)
    else:
        return "Invalid operator"

#user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Calculate and display the result
result = calculate(num1, num2, operator)
print("Result: ", result)
