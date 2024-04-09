OgAlfabetsLista = "abcdefghijklmnopqrstuvwxyzåäö"

beforechange = input()
AmountOfLetters = 30
steps = 2
reset = -29
position = ""

for bokstav in beforechange:
    position += OgAlfabetsLista[OgAlfabetsLista.index(bokstav) + steps]
    if position + steps >= 30:
        position= (position + steps) + reset

print(position)