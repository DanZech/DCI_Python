def make_pretty(func):
    def inner():
        print('I am decorator')
        func()
    return inner

def my_regulr_func():
    print('Hello World')

pretty = make_pretty(my_regulr_func)
#pretty()

def make_upper(func):
    def inner():
        return func().upper()
    return inner

@make_upper
def greeting():
    return 'Hello World'

# print(greeting())

def make_count(func):
    def inner():
        return str(len('Hello World'))
    return inner

def make_split(func):
    def inner():
        return func().split()
    return inner

@make_count
@make_split
def ordinary():
    return 'Hello World'

print(ordinary())