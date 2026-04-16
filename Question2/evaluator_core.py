# This file handles the actual calculation of the parse tree
# Once the tree is built by parser.py, this file walks through it
# and computes the final numeric result
# I also included format_tree here to display the tree as a string

def format_tree(node):
    # Display a number node as just its value
    if node[0] == 'num':
        return str(node[1])
    # Display unary negation
    if node[0] == 'neg':
        return f'(neg {format_tree(node[1])})'
    # Display binary operations like (+ 3 5)
    return f'({node[0]} {format_tree(node[1])} {format_tree(node[2])})'


def evaluate(node):
    # Base case - just return the number
    if node[0] == 'num':
        return node[1]

    # Flip the sign for unary negation
    if node[0] == 'neg':
        return -evaluate(node[1])

    # Addition
    if node[0] == '+':
        return evaluate(node[1]) + evaluate(node[2])

    # Subtraction
    if node[0] == '-':
        return evaluate(node[1]) - evaluate(node[2])

    # Multiplication
    if node[0] == '*':
        return evaluate(node[1]) * evaluate(node[2])

    # Division - I check for zero here to avoid crashes
    if node[0] == '/':
        right = evaluate(node[2])
        if right == 0:
            raise ZeroDivisionError("Division by zero")
        return evaluate(node[1]) / right