from timeit import default_timer as timer
my_list = [x for x in range(100000001)]
start = timer()
for i in my_list:
    if i == 100000000:
        break
end = timer()
print(f'Liner search: {end - start}')

def bin_search(my_list, item):
    low = 0
    high = len(my_list) - 1
    step = 0
    while low <= high:
        step += 1
        mid = round((low + high) / 2)
        guess = my_list[mid]
        if guess == item:
            return step
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None