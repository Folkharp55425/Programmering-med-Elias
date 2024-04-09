input("\nStäll en fråga så besvarar jag den... ")

import random

nej_svar_lista = ["Definitivt inte!", "Svaret har alltid varit & kommer för evigt kvarstå som, NEJ!", "Glöm din dröm!", "Hoppades du på ett Ja, så beklagar jag sorgen..." ]
ja_svar_lista = ["Absolut!", "Svaret har alltid varit & kommer för evigt förbli, JA!", "Du kan ge dig fan på att !", "Hoppades du på ett Ja, så vill jag gratulera dig!"]
alternativ_svar_lista = ["Din magkänsla har korrekt!", "Det är väldigt oklart än så länge", "inte änns gud hade kunnat svara på det.", "Du får tänka själv denna gång. Jag är upptagen med din morsa."]
svar_alternativ = [nej_svar_lista, ja_svar_lista, alternativ_svar_lista]

x = random.choice(svar_alternativ)
print("\n",(random.choice(x)),"\n")