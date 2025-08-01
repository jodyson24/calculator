import math

first_operand = input("Enter a number: ")
operator = input("Enter an operator (+, -, *, /, %, ^, sqrt): ")
second_operand = input("Enter a second number (or leave blank for sqrt): ")


def calculator(first_operand, operator, second_operand):
    try:
        first_operand = float(first_operand)

        if (second_operand):
            second_operand = float(second_operand)

        if operator == "+":
            return first_operand + second_operand
        elif operator == "-":
            return first_operand - second_operand
        elif operator == "*":
            return first_operand * second_operand
        elif operator == "/":
            if second_operand == 0:
                return "Error: Division by zero"
            return first_operand / second_operand
        elif operator == '%':
            return first_operand % second_operand
        elif operator == '^':
            return first_operand ** second_operand
        elif operator == 'sqrt':
            return math.sqrt(first_operand)
        else:
            return "Invalid operator"
    except ValueError:
        return "Invalid input, please enter numbers only"
    

result = calculator(first_operand, operator, second_operand)

print("Result: ", result)