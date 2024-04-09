texten_innan = input()
texten_efter = ""

for bokstav in texten_innan:
    if bokstav == "A" or bokstav == "I" or bokstav == "O" or bokstav == "U" or bokstav == "Y" or bokstav == "Å" or bokstav == "Ä" or bokstav == "Ö" 
        texten_innan += "E"
    else:
        texten_innan += bokstav

print(texten_efter)