from data2 import stock
from datetime import datetime, timedelta
import pytz

'''
stock = [
    {"state": "Almost new", "category": "Keyboard",
     "warehouse": 1, "date_of_stock": "2020-05-06 08:28:12"},
    {"state": "Funny", "category": "Smartphone",
     "warehouse": 1, "date_of_stock": "2020-10-26 18:46:51"},
    {"state": "Brand new", "category": "Mouse",
     "warehouse": 1, "date_of_stock": "2021-03-26 06:57:23"},
    {"state": "Brand new", "category": "Monitor",
     "warehouse": 2, "date_of_stock": "2022-01-15 12:02:37"},
    {"state": "Almost new", "category": "Printer",
     "warehouse": 2, "date_of_stock": "2022-02-01 14:17:58"},
    {"state": "Refurbished", "category": "Laptop",
     "warehouse": 2, "date_of_stock": "2022-02-20 16:44:29"}
]
'''

warehouse1 = []
warehouse2 = []

def logistic():
    for i in stock:
        if i["warehouse"] == 1:
            item_name = i["state"] + ' ' + i["category"]
            warehouse1.append(item_name)
        else:
            item_name = i["state"] + ' ' + i["category"]
            warehouse2.append(item_name)
    return warehouse1, warehouse2
    

def total_items():
    logistic()   
    counter = 0
    print('\nInventory warehouse n.01\n')
    for item in warehouse1:
        counter += 1
        print(f'{counter}. {item}')
    print('\nInventory warehouse n.02\n')
    for item in warehouse2:    
        counter += 1
        print(f'{counter}. {item}')
#total_items()


def get_current_utc_datetime():
    return datetime.now(pytz.utc)
# print(get_current_utc_datetime())


def stock_time_control():
    for i in stock:
        if i["warehouse"] == 1:
            item_name = i["state"] + ' ' + i["category"]+ ', '+ i["date_of_stock"]
            warehouse1.append(item_name)
        else:
            item_name = i["state"] + ' ' + i["category"]+', ' + i["date_of_stock"]
            warehouse2.append(item_name)
    return warehouse1, warehouse2


def calculate_item_age_in_days(date_of_stock):
    for i in stock:
        date_of_stock_datetime = datetime.strptime(
            date_of_stock, '%Y-%m-%d %H:%M:%S').replace(tzinfo=pytz.utc)
        current_datetime = get_current_utc_datetime()
        age_in_days = (current_datetime - date_of_stock_datetime).days
        return age_in_days
        print(age_in_days)




'''
user_name = input('Username: ')

while len(user_name) <= 1:
  print('Please write your name!')
  user_name = input('Username: ')

print(
    f'\nHello {user_name}\n\n\
    Choose an option:\n\
    1. List items by warehouse;\n\
    2. Search an item and place an order;\n\
    3. Quit;\n'
)

# List of dictionaries representing the stock.



def ordering(w3, item_name):
    if w3 == 0:
        print('Bye')
    else:
        order = input('Would you like to order this item? (y/n) ')
        if order == 'y':
            try:
                qtde = int(input('How many would you like? '))
                if qtde <= w3:
                    print('Thank you very much for your preference buying with us.')
                elif qtde > w3:
                    print(f'\n**************************************************\n\
                        There are not this many available.\n\
                        The maximum amount that can be ordered is {w3}\n\
                        **************************************************\n')
                    order = input(
                        f'Would like to order all {w3} items we have in stock? (y/n) ')
                    if order == 'y':
                        print(
                            f'Thank you very much for buying all {w3} {item_name}.')
                    elif order == 'n':
                        qtde = int(input(
                            f'Inform the amount of {item_name} less than {w3} that you would like to order: '))
                        print(
                            f'Thank you for ordering {qtde} {item_name} with us.')
            except:
                print('Invalid Character')
        elif order == 'n':
            print('Thank you for visiting')
        else:
            print('Invalid Character')


while True:
    p = input('Enter your choice: ')
    o = 0
    if p == '1':
        print('\nItems from warehouse 1: \n')
        for item in stock:
            if item["warehouse"] == 1:
                o += 1
                print(f'{o}. {item["category"]}')
        print('\nItems from warehouse 2: \n')
        for item in stock:
            if item["warehouse"] == 2:
                o += 1
                print(f'{o}. {item["category"]}')

    elif

'''
