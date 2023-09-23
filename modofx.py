

# x = the given modulus

Lists = [numbers given to get the mod of]

Library = "list of words/numbers/symbols to match with the remainder of the modulus"

for remainder in Lists:
    print(Library[remainder % x],end="")



#example:-

Lists = [128,322,353,235,336]

Library = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

for remainder in Lists:
    print(Library[remainder %37],end="")