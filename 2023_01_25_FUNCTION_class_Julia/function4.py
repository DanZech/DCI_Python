names = {'name1': 'Jaman', 'name2': 'Susan', 'name3': 'John'}
num = [800, 200, 300, 500] 

def greet(*args, **kwargs):
    n1 = kwargs['name1']
    n2 = kwargs['name2']
    c = args[0] + args[1]

    return f'Good morning,{n1} and {n2}', c

print(greet(*num, **names))


