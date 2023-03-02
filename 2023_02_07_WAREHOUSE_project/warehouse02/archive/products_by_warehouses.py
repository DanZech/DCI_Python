from data2 import stock


def products_by_warehouses():
    warehouse1 = []
    warehouse2 = []

    for i in stock:
        if i['warehouse'] == 1:
            item_name = i['state'] + ' ' + i['category']
            warehouse1.append(item_name)
        else:
            item_name = i['state'] + ' ' + i['category']
            warehouse2.append(item_name)