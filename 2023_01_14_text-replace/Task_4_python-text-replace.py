'''
Write a program that replaces the standalone "dog" in the following sentence with "cat". 
Use f-string when printing the output.
Input:
"A dogmatic dog buys dogecoin to become rich and buy hotdogs every day." 
Output:
A dogmatic cat buys dogecoin to become rich and buy hotdogs every day.

'''

txt = "A dogmatic dog buys dogecoin to become rich and buy hotdogs every day."
txt_1 = txt.replace('dog', 'cat', 2)
txt_2 = txt_1.replace('cat', 'dog', 1)
print(txt_2)
