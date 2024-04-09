class Pokemon:
    def __init__(self, name, element, hp, defence, attack, evolution):
        self.name = name
        self.element = element
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.evolution = evolution

pokemon1 = Pokemon("Sandshrew", "Ground", "50", "85", "75", "First_gen" )