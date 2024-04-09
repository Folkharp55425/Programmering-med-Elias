def add_on_21(): 

    total_summa = 0

    while total_summa < 21:

        while True:
            term1 = int(input("Player1, Choose a number from 1-3."))

            if term1 not in [1,2,3]:
                print("\nInvalid value entered. Try to enter 1, 2 or 3.")
                        
            else:
                total_summa += term1
                print("\nThe value is:", (total_summa))
                break

        if total_summa > 21:
            print("You've lost!")
            break
            
        elif total_summa == 21: 
            print("Player1, has won!")
            break
        
        while True:
            term2 = int(input("Player2, Choose a number from 1-3."))

            if term2 not in [1,2,3]:
                print("\nInvalid value entered. Try to enter 1, 2 or 3.")
                        
            else:
                total_summa += term2
                print("\nThe value is:", (total_summa))
                break

        if total_summa > 21:
            print("You've lost!")
            break

        elif total_summa == 21: 
            print("Player2, has won!")
            break
while True:
    choice = input('Do you want to play "Add on 21" Y/N ')

    if choice == "Y" or choice == "y":
        add_on_21()

    elif choice == "N" or choice == "n":
        exit()
    else:
        print("Answer with Y or N.")