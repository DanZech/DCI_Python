#Task_1
a1=234
a2=43.12
a3=(3+2j)
a4='Hello'
a5=10>5
print(a1, a2, a3, a4, a5, sep="\n")

#task2
print()
print(f'{a1} is type of {type(a1)}')
print(f'{a2} is type of {type(a2)}')
print(f'{a3} is type of {type(a3)}')
print(f'{a4} is type of {type(a4)}')
print(f'{a5} is type of {type(a5)}')


#task3
print()
n1=123 #int
n2=43.23 #float
n3=(10>5) #bool
n4=(3+2j) #complex
n5=("Mandela") #str
print(isinstance(n1, int)) #true
print(isinstance(n2, int)) #false
print(isinstance(n3, bool)) #true
print(isinstance(n4, complex)) #true
print(isinstance(n5, int)) #false

#task4

''' 

Task5

testing if the var is a certain kind of type
Using the "isinstance()" function

'''
print()
n1=123 #int
n2=43.23 #float
n3=(10>5) #bool
n4=(3+2j) #complex
#n5=("Mandela") #str
n6=('"How are you?"') #str
print(f'Is {n1} an instance of int? {isinstance(n1 , int)}') #true
print(f'Is {n2} an instance of bool? {isinstance(n2, int)}') #false
print(f'Is {n4} an instance of complex? {isinstance(n4, complex)}') #true
print(f'Is {n3} an instance of bool? {isinstance(n3, bool)}') #true
print(f'Is {n6} an instance of float? {isinstance(n6, int)}') #false
print()

print('task 5: comment done for task 4. Please, check the code.')
print()