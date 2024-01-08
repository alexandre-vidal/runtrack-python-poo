class Personnage:
    def __init__(self, x, y, perso):
        self.x = x
        self.y = y
        self.perso = perso
    
    def afficherX(self):
        return f"X = {self.x}"
        
    def afficherY(self):
        return f"Y = {self.y}"