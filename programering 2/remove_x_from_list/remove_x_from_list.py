the_list = []

cancel_out = ' '
cancel_out_add = ' '

def add_to_list1():
    add_to = input("what do you want to add?\n: ")
    the_list.append(add_to)

def add_to_list2():
    global cancel_out_add
    cancel_out_add = str(input("what do you want to remove? "))
    
    return cancel_out_add
    
    

def remove_it():

    list_string = [str(e) for e in the_list]

    list_string.remove(cancel_out)

    print(list_string)

def question2():
    global cancel_out
    global cancel_out_add
    while True:
        cancel_out += cancel_out_add
        print("cancel out list is: ", cancel_out)
        choice2 = input("Do you want to add on the cancel out list? Y/N\n: ")

        if choice2 == "y" or choice2 == "y":
            add_to_list2()
        else:
            remove_it()

while True:
    print("base list is: ", the_list)
    choice1 = input("Do you want to add to the base list? Y/N\n: ")

    if choice1 == "y" or choice1 == "y":
        add_to_list1()
    else:
        question2()
