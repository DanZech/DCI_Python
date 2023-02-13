from data import warehouse1, warehouse2
#from daniel import ordering

user_name = input('Username: ')
while (len(user_name) <= 1):
  print('Please write your name!')
  user_name = input('Username: ')
  
print(
    f'\nHello {user_name}\n\nChoose an option:\n1. List items by warehouse;\n2. Search an  item and place an order;\n3. Quit;\n'
  )


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
          print(
          f'\n**************************************************\nThere are not this many available.\nThe maximum amount that can be ordered is {w3}\n**************************************************\n'
          )
          order = input(
            f'Would like to order all {w3} items we have in stock? (y/n) ')
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
  o = 0
  if p == '1':  #List items by warehouse
    print('\nItems from warehouse 1: \n')
    for i in warehouse1:
      o += 1
      print(f'{o}. {i}')
    print('\nItems from warehouse 2: \n')
    for j in warehouse2:
      o += 1
      print(f'{o}. {j}')
      #print(f'\nThanks for your visit, {user_name}')

  elif p == '2':  #Search an item and place an order
    item_name = input('Enter an item name: ')
    w1 = warehouse1.count(item_name)
    w2 = warehouse2.count(item_name)
    w3 = w1 + w2
    print(f'\nTotal amount of items in both warehouses: {w3}')
    if w1 > 0 and w2 > 0:
      print('Location: both warehouse\n')
    elif w1 > 0 and w2 == 0:
      print('Location: warehouse 1\n')
    elif w1 == 0 and w2 > 0:
      print('Location: warehouse 2\n')
    else:
      print('Not in stock')

    ordering(w3, item_name)
    
  elif p == '3':
    print('Thank you for you visit')
    break

  else:
    print('invalid Character')

  print('\nChoose an option:\n1. List items by warehouse;\n2. Search an  item and place an order;\n3. Quit;\n')