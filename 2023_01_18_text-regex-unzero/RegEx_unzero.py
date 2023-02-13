'''
Create a function that takes a string input as a number and replaces leading and trailing zeros.
Input/Output:
"0023.07623070"   -->   "23.0762307"  
"hello world"     -->   "hello world"  
"01230"           -->   "1230"  
'''

import re

string = input()

def remove_leading_trailing_zeros(string):
    # Use a regular expression to match leading zeros
    leading_zeros_regex = r"^0+(?=\d)"
    # Use the re.sub() function to remove leading zeros
    string = re.sub(leading_zeros_regex, "", string)
    # Use a regular expression to match trailing zeros
    trailing_zeros_regex = r"(?<=\d)0+$"
    # Use the re.sub() function to remove trailing zeros
    string = re.sub(trailing_zeros_regex, "", string)
    return string

print(remove_leading_trailing_zeros(string))  
#print(remove_leading_trailing_zeros("0023.07623070"))   # "23.0762307"
#print(remove_leading_trailing_zeros("hello world"))     # "hello world"
#print(remove_leading_trailing_zeros("01230"))           # "1230"