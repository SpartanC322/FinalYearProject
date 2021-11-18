class Enemy:
    enemyClass = ""
    health = 0
    damage = 0

    def __init__(self, enClass, hp, dam):
        self.enemyClass = enClass
        self.health = hp
        self.damage = dam

