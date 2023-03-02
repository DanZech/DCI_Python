from data2 import stock

'''
stock = [
    {"state": "Almost new", 
    "category": "Keyboard", 
    "warehouse": 1, 
    "date_of_stock": "2020-05-06 08:28:12"}, 
    
    {"state": "Funny", 
    "category": "Smartphone", 
    "warehouse": 1, 
    "date_of_stock": "2020-10-26 18:46:51"}, 
    
    {"state": "Brand new", 
    "category": "Mouse", 
    "warehouse": 1, 
    "date_of_stock": "2021-03-26 06:57:23"}, 
    
    '''

user_name = input('Username: ' )
print(f'\nHello {user_name}\n\nChoose an option:\n1. List items by warehouse;\n2. Search an item and place an order;\n3. Quit;\n')
p = int(input('Enter your choise: '))

def ordering():
    order = input('Would you like to order this item?(y/n) ')
    if order == 'y':
        qtde = int(input('How many would you like? '))
        if qtde <= w3:
            print('Thank you very much for your preference buying with us.') 
        elif qtde > w3:
            print(f'\n**************************************************\nThere are not this many available.\nThe maximum amount that can be ordered is {w3}\n**************************************************\n')
            order = input(f'Would like to order all {w3} items we have in stock? (y/n) ')
            if order == 'y':
                print(f'Thank you very much for buying all {w3} {item_name}.') 
            elif order == 'n':
                qtde = int(input(f'Inform the amout of {item_name} less than {w3} that you would like to order: '))
                print(f'Thank you for ordening {qtde} {item_name} with us.')
    elif order == 'n':
        print('Thank you for you visit')


# separe items by warehouses 1 & 2
warehouse1 = []
warehouse2 = []
for i in stock:
    counter1=0
    counter2 = 0
    if i["warehouse"] == 1:
        counter1 += 1
        item_name1 = (i["state"] + ' '+i["category"]).lower()
        warehouse1.append(item_name1)
for j in stock:
    if j["warehouse"] == 2:
        counter2 += 1
        item_name2 = (j["state"] + ' '+j["category"]).lower()
        warehouse2.append(item_name2)



if p == 1: #List items by warehouse
    counter1 = 0
    print('\nItems from warehouse 1: \n')
    for i in stock:
        if i["warehouse"] == 1:
            counter1 += 1
            item_name = i["state"]+ ' '+i["category"]        #+ ', in stock since '+i["date_of_stock"]
            print(f'{counter1}. {item_name}')
            warehouse1.append(item_name1)
    
    print(f'\nTotal itens in warehouse 1: {counter1}')
         
    print('\nItems from warehouse 2: \n')
    counter2 = 0
    for j in stock:
        if j["warehouse"] == 2:
            counter2 += 1
            item_name = j["state"] + ' '+j["category"]     
            print(f'{counter2}. {item_name}')
            warehouse2.append(item_name2)
            
    print(f'\nTotal itens in warehouse 2: {counter2}')
    print(f'\nTotal amount of items in stock: {counter1 + counter2}')
    print(f'\nThank you for your visit, {user_name}')


#Search an item and place an order
elif p == 2: 
    product = input('What is the item name: ').lower()
        
    w1 = warehouse1.count(product)
    w2 = warehouse2.count(product)
    w3 = w1 + w2

    print(f'\nAmount available: {w3}')
    print('Location:')
    if w1 > 0 and w2 > 0:

        print('Location: both warehouse\n')
    elif w1 > 0 and w2 == 0:
        print('Location: warehouse 1\n')        
    elif w1 == 0 and w2 > 0:
        print('Location: warehouse 2\n')
    else:
        print('Not in stock')


#ordering()

    #p = int(input('\nPress n. 2 to search an item and place an order,\nor press n. 3 to Quit\n\nEnter your choise: '))

