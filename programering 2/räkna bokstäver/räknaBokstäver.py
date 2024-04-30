def separate():

    dictionary = {}

    WhatToCount = input("Enter text to count: ").replace(" ", "")

    for bokstav in WhatToCount:
        if bokstav in dictionary:
            dictionary[bokstav] += 1
        else:
            dictionary[bokstav] = 1

    print(dictionary)

def combined():
    
    dictionary = {}

    WhatToCount = input("Enter text to count: ").replace(" ", "").upper()



    for bokstav in WhatToCount:
        if bokstav in dictionary:
            dictionary[bokstav] += 1
        else:
            dictionary[bokstav] = 1

    print(dictionary)

while True:
    CombOrNot = input ("Would you like to combine lower and upper case letters Y/N?\n")

    if CombOrNot == "Y" or CombOrNot == "y":
        combined()
    
    elif CombOrNot == "N" or CombOrNot == "n":
        separate()