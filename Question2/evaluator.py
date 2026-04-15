def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        char = expression[i]

        # skip the spaces
        if char == ' ':
            i += 1
            continue

        # if number 
        if char.isdigit():
            num = ''
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(('NUM', int(num)))
            continue

        # if operator
        if char in '+-*/':
            tokens.append(('OP', char))
            i += 1
            continue

        # if left parenthesis
        if char == '(':
            tokens.append(('LPAREN', '('))
            i += 1
            continue

        # if right parenthesis
        if char == ')':
            tokens.append(('RPAREN', ')'))
            i += 1
            continue

        # if error
        return None

    # Add END token 
    tokens.append(('END', 'END'))
    return tokens


def format_tokens(tokens):
    result = ''
    for token_type, token_value in tokens:
        if token_type == 'END':
            result += '[END]'
        else:
            result += f'[{token_type}:{token_value}] '
    return result.strip()


def parse_primary(tokens, pos):
    token_type, token_value = tokens[pos]

    # if number
    if token_type == 'NUM':
        node = ('num', token_value)
        return node, pos + 1

    # if unary negation
    if token_type == 'OP' and token_value == '-':
        operand, pos = parse_primary(tokens, pos + 1)
        node = ('neg', operand)
        return node, pos

    # Iif left parenthesis
    if token_type == 'LPAREN':
        node, pos = parse_expression(tokens, pos + 1)
        if tokens[pos][0] != 'RPAREN':
            raise ValueError("Expected closing parenthesis")
        return node, pos + 1

    raise ValueError(f"Unexpected token: {token_value}")