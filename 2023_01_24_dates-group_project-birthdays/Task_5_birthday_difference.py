import datetime
from datetime import timedelta

first_birthday = input('Enter a birthdate in YYYY-MM-DD format: ')
year, month, day = map(int, first_birthday.split('-'))
date1 = datetime.date(year, month, day)

second_birthday = input('Enter a second birthdate in YYYY-MM-DD format: ')
year, month, day = map(int, second_birthday.split('-'))
date2 = datetime.date(year, month, day)


# def get_birthday_difference(first_birthday, second_birthday):
difference = date1 - date2
print(difference)