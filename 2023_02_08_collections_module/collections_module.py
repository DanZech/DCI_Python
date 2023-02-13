from collections import Counter, OrderedDict, ChainMap, namedtuple
fridge = ["Apple", "Apple", "Cabbage", "Steak", "Cheese", "Apple", "Carrtot"]
print(len(fridge))

my_count = Counter(fridge)
print(my_count)

lunch = Counter(Apple=2, Steak=2)
my_count.subtract(lunch)
print(my_count)

shopping = Counter(Flowers=3, Banana=5)
my_count.update(shopping)
print(my_count)

count1=Counter(Apple=3, Banana=2)
count2=Counter(Banana=1, Cheese=3) 
print(count1 + count2)
print(count1 - count2)
print(count1 & count2) #and 
print(count1 | count2) # or
print(count1 == count2) # boolean
print(count1 != count2) # bolean

my_dict = {
    "name":"Bob",
    "age": 56,
    "country": "Germany" 
}
my_ordered_dict = OrderedDict(my_dict)
print(my_ordered_dict)