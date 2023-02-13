fridge = ['Apple', 'Apple', 'Cabbage', 'Steak', 'Cheese', 'Apple', 'Carrot', 'Yougurt']
counter = {}

'''
for ingredient in fridge:
    if ingredient in counter:
        counter[ingredient] += 1
    else:
        counter[ingredient] = 0
'''

from collections import Counter
my_counter = Counter(fridge)
print(my_counter)
print(my_counter.total())


lunch = Counter(Carrot=1, Cabbage=2)
print(lunch)

my_counter.subtract(lunch)

shopping = Counter(Carrot=10, Beer=7, Cream=5)
my_counter.update(shopping)
print(my_counter)

print(my_counter.most_common())
