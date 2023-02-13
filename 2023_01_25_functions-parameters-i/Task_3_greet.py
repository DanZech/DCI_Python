def greet(tempo):
    if tempo >= 6 and tempo <= 12:
        print('Good Morning!')
    elif tempo > 12 and tempo <= 18:
        print('Good afternoon!')
    else:
        print('Good evening!')

greet(7)
greet(14)
greet(21)

'''
print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
    ))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
    ))
    
    '''