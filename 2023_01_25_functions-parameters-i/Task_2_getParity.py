def getParity(num, parity):
    if parity == "odd":
        return num % 2 != 0
    elif parity == "even":
        return num % 2 == 0
    else:
        return "Parity indicated is unknown"

print(getParity(1, "odd"), getParity(2, "odd") ) # True False
print(getParity(1, "even"), getParity(1, "odd")) # False True
print(getParity(11, "even"), getParity(11, "odd")) # False True
print(getParity(-2, "unknown")) # Parity indicated is unknown