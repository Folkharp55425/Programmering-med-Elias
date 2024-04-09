word = ""
str1 = word
str2 = ""

def Restart():
    global word
    global str2
    global word
    
    not_number = True

    while not_number:
        word = input("Är det en Palindrom?: ")
    
        for letter in reversed(word):
                
            if letter.isnumeric() == True:
                print(" Use only letters\n Restarting script...")
                not_number = False
                Restart()
                

            elif letter.isnumeric() == False: 
                str2 += letter
                not_number = True
        CheckIfPalindrom()


def CheckIfPalindrom():
    global str1
    global str2
    global word

    print(str1)

    if word.lower() == str2.lower():
        print("ditt ord är en Palindrom!")
        

    else:
        print("Ditt ord är ingen Palindrom")

Restart()