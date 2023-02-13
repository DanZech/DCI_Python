'''Create a function that takes a string input and checks if it is a mathematical expression. 
Supported operators: +, -, *, /, % and only integers

Input/Output:
"5 + 2"         -->    true  
"9 * 1"         -->    true  
"hello world"   -->    false  
"123"           -->    false  
"5 + foo"       -->    false  
'''

import re

def is_math_expression(string):
    # Use a regular expression to match a mathematical expression
    math_expression_regex = r"^\d+([\+\-\*/\%]\d+)*$"
    # Use the re.search() function to check if the string matches the pattern
    match = re.search(math_expression_regex, string)
    return match is not None

print(is_math_expression("5 + 2"))         # True
print(is_math_expression("9 * 1"))         # True
print(is_math_expression("hello world"))   # False
print(is_math_expression("123"))           # False
print(is_math_expression("5 + foo"))       # False