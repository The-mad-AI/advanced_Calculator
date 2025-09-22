class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        
    def attack(self):
        print(f"{self.name} attacks with basic strike!")
        
        
class Wizard(Player):
    def attack(self):
        print(f"{self.name} casts a fireball!")
        

p1 = Player("Hero", 100)
p2 = Wizard("Gandalf", 80)

p1.attack()
p2.attack()