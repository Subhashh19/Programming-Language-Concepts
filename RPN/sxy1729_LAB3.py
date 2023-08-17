'''
Name: Sai Subhash Yalamadala 
UTA ID: 1002031729
Date: 28 July 2023
OS: macOS 
'''
import os

def is_operator(token):
    return token in ['+', '-', '*', '/']

# Function to apply the specified operator to operands and return result
def apply_operator(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def evaluate_rpn(expression):
    # Function to evaluate an RPN expression 
    stack = []
    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        elif is_operator(token):
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = apply_operator(operand1, operand2, token)
            stack.append(result)
        else:
            raise ValueError("Invalid token in expression: " + token)

    # The final result will be the only element left on the stack
    return stack[0]

def main():
    input_file = os.path.join(os.path.dirname(__file__), 'input_RPN.txt')
    with open(input_file, 'r') as file:
        expressions = file.read().splitlines()

    for expression in expressions:
        result = evaluate_rpn(expression)
        print(result)

if __name__ == "__main__":
     # Calling the main function
    main()