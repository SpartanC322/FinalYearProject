

class Servant:

    servClass = ""
    servHealth = 0
    np = 0
    servDamage = 0
    cards = []

    def __init__(self, servClass, servHealth, np, servDamage, cards):
        self.servClass = servClass
        self.servHealth = servHealth
        self.np = np
        self.servDamage = servDamage
        self.cards = cards
        