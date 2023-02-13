
def isOdd(num):
    if num == 0:
        return False
    elif num % 3 == 0 or num == 1:
        return True
    else:
        return False
        
def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))