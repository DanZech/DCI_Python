from data2 import stock
from datetime import datetime as dt

user_name = input('Username: ')  # 1. The user is asked to provide a name.
while (len(user_name) <= 1): # avoid an empty username
  print('Please write your name!')
  user_name = input('Username: ')

#  The user is greeted by its name.
print(f'\nHello {user_name}\n\n\
      \
    Choose an option:\n\
    1. List items by warehouse;\n\
    2. Search an  item and place an order;\n\
    3. Quit;\n')  # menu is printed out showing 3 options


warehouse1 = []
warehouse2 = []

def ordering(w3, item_name):

  if w3 == 0:
    print('Bye')
  else:
    order = input('Would you like to order this item?(y/n) ')
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

          order = input(f'Would like to order all {w3} items we have in stock? (y/n) ')

          if order == 'y':
            print(f'Thank you very much for buying all {w3} {item_name}.')
          elif order == 'n':
            qtde = int(
              input(
                f'Inform the amout of {item_name} less than {w3} that you would like to order: '
              ))
            print(f'Thank you for ordening {qtde} {item_name} with us.')
      except:
        print('Invalid Character')
    elif order == 'n':
      print('Thank you for you visit')

    else:
      print('Invalid Character')


while True: 
  
  p = input('Enter your choise: ')
  p = p.lower()                                       # turn input item in case insensitive
  o = 0                                               # variable for the total counter
  if p == '1':  #List items by warehouse
    print('\nItems from warehouse 1: \n') 
    for item in stock:
      if item['warehouse'] == 1:
        o += 1                                        # item counter
        print(f'{o}. {item["category"]}')

    print('\nItems from warehouse 2: \n')
    for item in stock:
      if item['warehouse'] == 1:
        o += 1                                        # item counter
        print(f'{o}. {item["category"]}')
            
      #print(f'\nThanks for your visit, {user_name}')

  elif p == '2':  #Search an item and place an order
    item_name = input('Enter an item name: ')
    w1 = stock.count(item_name)
    w2 = stock.count(item_name)
    w3 = w1 + w2
    print(f'\nTotal amount of items in stock: {w3}')

    if w1 > 0 and w2 > 0:
      print('\nLocation: both warehouse\n')
    elif w1 > 0 and w2 == 0:
      print('\nLocation: warehouse 1\n')
    elif w1 == 0 and w2 > 0:
      print('\nLocation: warehouse 2\n')
    else:
      print('Not in stock')

    ordering(w3, item_name) #call the function to place an order of item
    
  elif p == '3':
    print('Thank you for you visit')
    break

  else:
    print('invalid Character')

  print('\nChoose an option:\n\
    1. List items by warehouse;\n\
    2. Search an  item and place an order;\n\
    3. Quit;\n')