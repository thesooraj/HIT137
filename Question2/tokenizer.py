# This file handles breaking down a math expression into tokens
# Each token is a small piece like a number, operator, or bracket
# I built this as the first step before parsing can happen

def tokenize(expression):
    # Start with empty list and go through each character one by one
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]

        # Skip any spaces between numbers and operators
        if char == ' ':
            i += 1
            continue

        # If I find a digit, keep reading until the full number is captured
        if char.isdigit():
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(('NUM', int(num)))
            continue

        # Check for basic math operators
        if char in '+-*/':
            tokens.append(('OP', char))
            i += 1
            continue

        # Opening bracket
        if char == '(':
            tokens.append(('LPAREN', '('))
            i += 1
            continue

        # Closing bracket
        if char == ')':
            tokens.append(('RPAREN', ')'))
            i += 1
            continue

        # If I reach here, the character is unknown so return None for error
        return None

    # Mark the end of the expression
    tokens.append(('END', 'END'))
    return tokens


def format_tokens(tokens):
    # This turns the token list into a readable string for output
    result = ''
    for token_type, token_value in tokens:
        if token_type == 'END':
            result += '[END]'
        else:
            result += f'[{token_type}:{token_value}] '
    return result.strip()