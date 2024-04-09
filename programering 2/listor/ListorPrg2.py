lista1 = []
lista2 = []

def AddToList1():

    expand1 = input("lista 1: ")
    lista1.append(expand1)

    

def AddToList2():

    expand2 = input("lista 2: ")
    lista2.append(expand2)


def addlistor():
    print("lista 1 then lista 2")

    joinedlist = lista1 + lista2
    print(joinedlist)


while True:
    
    choice1 = input("Do you want to add on the list Y/N: ")

    if choice1 == "Y" or choice1 == "y":
                
        while True:
            choice2 = input("\nWhich list?\n 1 or 2: ")

            if choice2 == "1":
                AddToList1()
                break

            elif choice2 == "2":
                AddToList2()
                break

            elif choice2 == "N" or choice2 == "n":
                addlistor()
                break

            else:
                print("\nOBS!! only choice available is 1, 2 or N to combine the lists")
                    
    elif choice1 == "N" or choice1 == "n":
        addlistor()           
            
    else:
        print("answer with Y/N")