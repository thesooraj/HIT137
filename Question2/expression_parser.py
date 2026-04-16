# This file handles parsing the tokens into a tree structure
# The tree shows the order of operations clearly
# I split it into three functions based on operator precedence

from tokenizer import format_tokens


def parse_primary(tokens, pos):
    token_type, token_value = tokens[pos]

    # If its a number just return it as a leaf node
    if token_type == 'NUM':
        return ('num', token_value), pos + 1

    # Handle unary minus like -5 or -(3+4)
    if token_type == 'OP' and token_value == '-':
        operand, pos = parse_primary(tokens, pos + 1)
        return ('neg', operand), pos

    # Handle expressions inside brackets
    if token_type == 'LPAREN':
        node, pos = parse_expression(tokens, pos + 1)
        if tokens[pos][0] != 'RPAREN':
            raise ValueError("Expected closing parenthesis")
        return node, pos + 1

    raise ValueError(f"Unexpected token: {token_value}")


def parse_term(tokens, pos):
    # Handle multiplication and division first
    left, pos = parse_primary(tokens, pos)
    while tokens[pos][0] == 'OP' and tokens[pos][1] in '*/':
        op = tokens[pos][1]
        right, pos = parse_primary(tokens, pos + 1)
        left = (op, left, right)
    return left, pos


def parse_expression(tokens, pos):
    # Handle addition and subtraction last
    left, pos = parse_term(tokens, pos)
    while tokens[pos][0] == 'OP' and tokens[pos][1] in '+-':
        op = tokens[pos][1]
        right, pos = parse_term(tokens, pos + 1)
        left = (op, left, right)
    return left, pos