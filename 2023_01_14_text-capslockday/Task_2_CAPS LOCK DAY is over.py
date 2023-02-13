'''
October 22nd is CAPS LOCK DAY. 
Apart from that day, every sentence should be lowercase, so write a function to normalize a sentence.
Create a function that takes a string. 
If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end. 
Each string is a normalized sentence and should start with an uppercase character.
'''

txt = input(('Enter here a sentence: '))
txt_capitalized = txt.capitalize()
print(txt_capitalized)