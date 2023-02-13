'''
Complete the function in the file src/task_6_number_sundays.py so that:
It takes the parameter date_string as a string in the format "Year-Month-Day"
It returns the number of Sundays since the birthdate date_string until the current day.

To test your code, run the command:

python src/test_6.py
'''

import datetime

first_birthday = input('Enter a birthdate in YYYY-MM-DD format: ')
year, month, day = map(int, first_birthday.split('-'))
date1 = datetime.date(year, month, day)

second_birthday = input('Enter a second birthdate in YYYY-MM-DD format: ')
year, month, day = map(int, second_birthday.split('-'))
date2 = datetime.date(year, month, day)

def total_sunday_counts(date_string):
    """
    This function will count the occurence of Sundays since the birthdate until the current date
    :param date_string: The birthdate
    :return: <int> Total occurence of sundays
    """
    # Write you code here
    pass