amount_c = [100, 50, 30, 5]

cost = int(input("Enter cost here: "))

def count_money(money_list, price):
    sum = 0
    sum += money_list[0] * 1 
    sum += money_list[1] * 2 
    sum += money_list[2] * 5 
    sum += money_list[3] * 10

    amount_back = sum - price

    if amount_back > 0:
        verification = True
        return [verification, amount_back]

    else:
        verification = False
        return [verification, sum]





result = count_money(amount_c, cost) 


        'print("Transaction completed!")
        'print("Your balance is:"(amount_back))

        'print("The transaction couldn't complete!")
        'print("Your balance is:"(sum))

    


