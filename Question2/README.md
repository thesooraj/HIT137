# Question 2 - Mathematical Expression Evaluator

## What this program does
This program reads mathematical expressions from a text file, evaluates each one, 
and writes the results to an output file. I built it using recursive descent parsing 
with no classes, only plain functions.

## File Structure

| File | Purpose |
|---|---|
| tokenizer.py | Breaks each expression into tokens like numbers, operators and brackets |
| expression_parser.py | Parses tokens and builds a tree showing order of operations |
| evaluator_core.py | Walks through the tree and calculates the final result |
| evaluator.py | Main file that ties everything together and handles file input/output |
| sample_input.txt | Input file containing test expressions |
| output.txt | Auto-generated output file with results |

## How to Run
Open terminal in this folder and type:

    python3 evaluator.py

## Input Format
One math expression per line in sample_input.txt. For example:

    3 + 5
    2 + 3 * 4
    -(3 + 4)

## Output Format
For each expression the program outputs exactly 4 lines followed by a blank line:

    Input: 3 + 5
    Tree: (+ 3 5)
    Tokens: [NUM:3] [OP:+] [NUM:5] [END]
    Result: 8

## Operators Supported
- Addition and subtraction with plus and minus
- Multiplication and division with star and slash
- Parentheses nested to any depth
- Unary negation like -5, --5, -(3+4)

## Error Handling
- Unknown characters like @ return ERROR for all fields
- Division by zero shows the tree but returns ERROR for result
- Unary plus is not supported and returns ERROR

## How the Code Works
1. tokenizer.py reads the expression character by character and creates a list of tokens
2. expression_parser.py takes those tokens and builds a tree structure respecting order of operations
3. evaluator_core.py walks the tree recursively and computes the answer
4. evaluator.py calls all of the above and writes the formatted output to output.txt