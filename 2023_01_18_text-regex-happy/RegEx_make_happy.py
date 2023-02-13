'''Make any face happy. Create a function that takes a sentence containing sad faces and turn them into happy ones! This involves changing only the mouths.
Make sure to only change the face if there are eyes before them, round(3.4) wouldn't become round)3.4) (for example).

Examples:
Sad face examples: :( 8( x( ;( Happy face examples: :) 8) x) ;)

Input / Output
make_happy("My current mood: :(")    -->    "My current mood: :)"  
make_happy("I was hungry 8(")        -->    "I was hungry 8)"  
make_happy("print('x(')")            -->    "print('x)')"  
'''

import re

def make_happy(sentence):
    # Use a regular expression to match sad faces that have eyes before them
    sad_face_regex = r"(?<=[:8x;])\("
    # Use the re.sub() function to replace the matched sad faces with happy faces
    happy_sentence = re.sub(sad_face_regex, ")", sentence)
    return happy_sentence

print(make_happy("My current mood: :("))    # "My current mood: :)"
print(make_happy("I was hungry 8("))        # "I was hungry 8)"
print(make_happy("print('x(')"))            # "print('x)')"