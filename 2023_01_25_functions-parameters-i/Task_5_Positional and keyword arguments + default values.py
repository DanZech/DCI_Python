# Positional and keyword arguments + default values


# string to words
    #If you have a string, you can subdivide it into several strings. 
    # The string needs to have at least one separating character, which may be a space.
    # By default the split method will use space as separator. 
    # Calling the method will return a list of all the substrings.

frase = 'Contrato com Limite de crédito'

def frase_separar():
    palavra = frase.split()
    print(palavra)
    
    
# String to characters
    # If you want to split a word into characters, use the list() method instead

def palavra_separar():
    letras = list(palavra)
    print(letras)


#def pig_latin(*long_dong): #PACKING. All arguments passed to pig_latin are packed into tuple *long_dong.
#    long_dong = list(long_dong) # Convert args tuple to a list so we can modify it

action = frase_separar()

    

