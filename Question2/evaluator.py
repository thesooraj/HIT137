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