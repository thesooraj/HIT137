# This is the main file that ties everything together
# It reads expressions from an input file line by line
# Then uses the tokenizer, parser and evaluator to process each one
# Finally it writes all results to output.txt in the required format

from tokenizer import tokenize, format_tokens
from expression_parser import parse_expression
from evaluator_core import evaluate, format_tree


def evaluate_file(input_path: str) -> list[dict]:
    import os

    # Build the output path in the same folder as input
    output_path = os.path.join(os.path.dirname(input_path), 'output.txt')
    results = []

    # Read all non-empty lines from the input file
    with open(input_path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    with open(output_path, 'w') as out:
        for i, line in enumerate(lines):

            # Step 1 - tokenize the expression
            tokens = tokenize(line)

            if tokens is None:
                # Unknown character found
                tree_str = 'ERROR'
                tokens_str = 'ERROR'
                result_str = 'ERROR'
                result_val = 'ERROR'
            else:
                try:
                    # Step 2 - parse tokens into a tree
                    tree, _ = parse_expression(tokens, 0)
                    tree_str = format_tree(tree)
                    tokens_str = format_tokens(tokens)

                    # Step 3 - evaluate the tree
                    result = evaluate(tree)

                    # Display whole numbers without decimal point
                    if result == int(result):
                        result_str = str(int(result))
                    else:
                        result_str = str(round(result, 4))
                    result_val = float(result)

                except ZeroDivisionError:
                    # Tree is still valid but result is error
                    tree_str = format_tree(tree)
                    tokens_str = format_tokens(tokens)
                    result_str = 'ERROR'
                    result_val = 'ERROR'

                except Exception:
                    # Any other error like unary + or bad syntax
                    tree_str = 'ERROR'
                    tokens_str = 'ERROR'
                    result_str = 'ERROR'
                    result_val = 'ERROR'

            # Write the four lines for this expression
            out.write(f'Input: {line}\n')
            out.write(f'Tree: {tree_str}\n')
            out.write(f'Tokens: {tokens_str}\n')
            out.write(f'Result: {result_str}\n')

            # Add blank line between expressions
            if i < len(lines) - 1:
                out.write('\n')

            results.append({
                'input': line,
                'tree': tree_str,
                'tokens': tokens_str,
                'result': result_val
            })

    return results


if __name__ == '__main__':
    results = evaluate_file('sample_input.txt')
    for r in results:
        print(r)