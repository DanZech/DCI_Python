from foods import foods

def cookable(foods):
    list_of_ingredients = []
    for food in foods:
        for ingredient in food['ingredients']:
            if ingredient['cooked']:
                list_of_ingredients.append(ingredient['item'])
    return list_of_ingredients
    
print(cookable(foods))

def uncookable(foods):
    list_of_ingredients = []
    for food in foods:
        for ingredient in food['ingredients']:
            if ingredient['cooked'] == False:
                list_of_ingredients.append(ingredient['item'])
    return list_of_ingredients

print(uncookable(foods))


