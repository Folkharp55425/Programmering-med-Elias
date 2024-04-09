
print(" För addition skriv 1 \n För subtraktion skriv 2")
print(" För multiplikation skriv 3 \n För division skriv 4 \n")

miniräknare = int(input("Välj miniräknare: "))

if miniräknare == 1:
    print("\naddition")
    term1 = int(input(" Term 1: "))
    term2 = int(input(" Term 2: "))
    summan = term1 + term2
    
    print(summan)

if miniräknare == 2:
    print("\nsubtraktion")
    term1 = int(input(" Term 1: "))
    term2 = int(input(" Term 2: "))
    summan = term1 - term2
    
    print(summan)

if miniräknare == 3:
    print("\nmultiplikation")
    term1 = int(input(" Term 1: "))
    term2 = int(input(" Term 2: "))
    summan = term1 * term2

    print(summan)

if miniräknare == 4:
    print("\ndivision")
    term1 = int(input(" Täljare: "))
    term2 = int(input(" Nämnare: "))
    summan = term1 / term2
    print(summan)
