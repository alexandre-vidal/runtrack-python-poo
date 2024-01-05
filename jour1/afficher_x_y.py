class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def afficherLesPoints(self):
        return f"X = {self.x} - Y = {self.y}"
        
    def afficherX(self):
        return f"X = {self.x}"
        
    def afficherY(self):
        return f"Y = {self.y}"
    
    def changerX(self):
        return f"X = {self.x + 5}"
        
    def changerY(self):        
        return f"Y = {self.y + 3}"

point = Point(10, 20)
print(point.afficherLesPoints())
print(point.afficherX())
print(point.afficherY())
print(point.changerX())
print(point.changerY())