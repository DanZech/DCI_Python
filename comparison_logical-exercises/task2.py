months30 = [4 , 6, 9, 11]
months28 = 2
months31 = [1, 3, 5, 7, 10, 12]
month = int(input('Digit a month number or 0 to quit: '))
while month != 0:
    if month in months30:
        print(30)
    elif month in months31:
        print(31)
    elif month == 2:
        year_bi = input('Is it a leap year (y or n): ')
        if year_bi == 'y':
            print(29)
        else:
            print(28)
    else:
        print('Please, digit a valid number (1 till 12), or 0 to quit:')
    month = int(input('Digit a month number:'))


