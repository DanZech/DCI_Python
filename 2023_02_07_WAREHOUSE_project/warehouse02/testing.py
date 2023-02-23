from data_warehouse2 import stock

'''
counter = 1
for cat in stock:
    print(cat["category"])
'''

wanted = {"state": "Brand new", "category": "Mouse"}
qtde = 0

for product in stock:
    if product["state"] == wanted["state"] and product["category"] == wanted["category"]:
       qtde += 1
       where = (product["warehouse"])


if qtde > 0:
    print(f"Prodcut in stock: {qtde}")
    print(where)



