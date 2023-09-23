
#To get the inverse mod of x

# x = the given modulus

Lists = [numbers given to get the mod of]

Library = "list of words/numbers/symbols to match with the remainder of the modulus"

for remainder in Lists:
    print(Library[pow(remainder, -1, x)],end="")



#example:-

Lists = [432,331,192,108,180,50]

Library = "=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"

for remainder in Lists:
    print(Library[pow(remainder, -1, 41)],end="")