'''Task 0: Extract birthday
Complete the function extract_birthday(date_str) in the file src/task_0 so that:
It accepts the parameter date_string in the format Year-Month-Day.
It returns a datetime.datetime object with the same month and year as date_string and with the current year.'''

from datetime import datetime
import calendar


def get_birthday(date_string, format='%Y/%m/%d'):
  # Write you code here
  return datetime.strptime(date_string, format)


date_string = "1984/06/06"
print(get_birthday(date_string))
print(type(get_birthday(date_string)))
'''
Task 1: Get the weekday of the birthdate
 In the file src/task_1_birthdate_weekday.py, complete the function get_weekday(date_string) so that:
It accepts the parameter date_string in the format Year-Month-Day.
It returns the weekday corresponding to the birthdate in date_string.
To test your code, run the command:

python src/test_1.py
'''


def get_weekday(date_string):
  # Write you code here
  bd = get_birthday(date_string)
  return bd.weekday(), calendar.day_name[bd.weekday()], bd.strftime('%A')


print(get_weekday(date_string))
'''
Task 2: Get the day number of the birthday
 In the file src/task_2_day_number_birthday.py, complete the function day_num_in_year(date_string) so that:
It accepts the parameter date_string in the format Year-Month-Day as the birthdate.
It returns the number of the day of the corresponding birthday in the current year.
Tip: You can use the function from src/task_0.
To test your code, run the command:

python src/test_2.py
'''


def day_num_in_year(date_string):
  """
    It returns day number of the birthday in the current year
    :param date_string:<str> birthdate in the format Year-Month-Day
    :return: <int> The day number
    """
  # Write you code here
  bd = get_birthday(date_string)
  print(type(bd.timetuple()))
  return bd.timetuple().tm_yday


print(day_num_in_year(date_string))
'''
Task 3: Get the weekday of the birthday

In the file src/task_3_birthday_weekday.py, complete the function get_weekday(date_string) so that:
It accepts the parameter date_string in the format Year-Month-Day.
It returns the weekday corresponding to the birthday in the current year of date_string.
To test your code, run the command:

python src/test_3.py
'''


def get_weekday(date_string):
  # Write you code here
  pass


'''
Task 4: Get the day number of the birthdate
 In the file src/task_4_day_number_birthdate.py, complete the function day_num_in_year(date_string) so that:
It accepts the parameter date_string in the format Year-Month-Day as the birthdate.
It returns the number of the day in the birth year.
For example if date_string is "1988-1-15", the function return 15.
For example if date_string is "2004-3-13", the function return 63. Note that 2004 is a leap year.

To test your code, run the command:

python src/test_4.py



import datetime
from task_0 import get_birthday


def day_num_in_year(date_string):
    """
    It returns day number of the birthdate in the birth year
    :param date_string:<str> birthdate in the format Year-Month-Day
    :return: <int> The day number
    """
    # Write you code here
    pass
'''
'''
Task 5: Difference in numbers between 2 birthdates
 Complete the function in the file src/task_5_day_difference.py so that:
It takes 2 parameters first_birthday and second_birthday as strings in the format "Year-Month-Day"
It returns the difference in days between the two birthdays.
To test your code, run the command:

python src/test_5.py
'''
'''
Task 6: Number of Sundays since a birthdate
 Complete the function in the file src/task_6_number_sundays.py so that:
It takes the parameter date_string as a string in the format "Year-Month-Day"
It returns the number of Sundays since the birthdate date_string until the current day.
To test your code, run the command:

python src/test_6.py

import datetime

def total_sunday_counts(date_string):
    """
    This function will count the occurence of Sundays since the birthdate until the current date
    :param date_string: The birthdate
    :return: <int> Total occurence of sundays
    """
    # Write you code here
    pass
'''
'''Task 9: Number of Days until the Next Birthday
 Complete the function in the file src/task_9_days_until_next_birthday.py so that:
It takes 2 parameters date_string and date_format as the birthdate and the date format respectively.
It returns the number of days until the next birthday
Notes:

You can calculate the week number manually, or you can use datetime.date.isocalendar to get it.
To test your code, run the command:

python src/test_9.py
'''


def calculate_dates(original_date, now):
  delta1 = datetime(now.year, original_date.month, original_date.day)
  delta2 = datetime(now.year + 1, original_date.month, original_date.day)

  if delta1 > now:
    r = delta1
  else:
    r = delta2

  #return ((delta1 if delta1 > now else delta2) - now).days
  return (r - now).days


def number_days(date_string, date_format='%Y/%m/%d'):
  """
    Returns the number of days until the next birthday
    :param date_string: The birthdate
    :param date_format: The format (recognized by datetime module)
    :return: The number of the days until the next birthday
    """
  # Write you code here
  bd = get_birthday(date_string)
  now = datetime.now()
  return calculate_dates(bd, now)


print(number_days(date_string))
'''
Task 10: List of Leap Years since Birthdate
 Complete the function in the file src/task_10_leap_years.py so that:
It takes 1 parameter date_string in the format "%Y-%m-%d" as the birthdate.
It returns a list of the leap years since the birthdate.
To test your code, run the command:

python src/test_10.py

import datetime
import calendar
'''


def get_leap_years(date_string):
  """
    Returns a list of the leap years since the birthdate
    :param date_string: The birthdate in the format "%Y-%m-%d"
    :return: A list of the leap years
    """

  # Write you code here
  bd = get_birthday(date_string).year
  now = datetime.now().year

  ylist = range(bd, now + 1)
  yleaps = []  #(), {}
  for y in ylist:
    if calendar.isleap(y):
      yleaps.append(y)

  return yleaps


print(get_leap_years(date_string))



book_dict = {}
book_dict['title'] = 'livro1'
print(book_dict)

book_dict['title'] = 'livro2'
print(book_dict)