from data2 import stock
from datetime import datetime
import pytz


def get_current_utc_datetime():
    return datetime.now(pytz.utc)

def calculate_item_age_in_days(date_of_stock):
    date_of_stock_datetime = datetime.strptime(
        date_of_stock, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc)
    current_datetime = get_current_utc_datetime()
    age_in_days = (current_datetime - date_of_stock_datetime).days
    print( age_in_days)


warehouse = []
def stock_time_control():
    for i in stock:
        item_name = i["state"] + ' ' + i["category"] + ', ' + i["date_of_stock"]
        warehouse.append(item_name)
    return warehouse

stock_time_control()
print(warehouse)

print(calculate_item_age_in_days("2022-02-20 16:44:29"))


'''
item = {
    "state": "Almost new",
    "category": "Keyboard",
    "warehouse": 1,
    "date_of_stock": "2020-05-06 08:28:12"
}
age_in_days = calculate_item_age_in_days(item["date_of_stock"])
print(age_in_days)
'''