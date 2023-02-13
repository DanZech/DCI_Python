def sumAll (*list):
    total = 0
    for i in list:
        for num in i:
            total += num
    return total


