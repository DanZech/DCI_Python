import datetime

def iterdates(date1, date2):
    one_day = datetime.timedelta(days = 1)
    current = date1
    while current < date2:
        yield current
        current += one_day

a = datetime.date(2018,1, 25)
b = datetime.date(2018, 2, 10)

for d in iterdates(a, b):
    if d.weekday() in (5, 6):
        for dia in d.weekday():
           
        	


#        print(d.weekday())
