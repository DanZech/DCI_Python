def make_pretty(func):
    def inner():
        print('I am decorator')
        func()
    return inner

def my_regulr_func():
    print('Hello World')

pretty = make_pretty(my_regulr_func)
pretty()