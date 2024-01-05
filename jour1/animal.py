class Animal:
    def __init__(self, prenom, age):
        self.prenom= prenom
        self.age = age
        
    def nommer(self):
        return f"L'animal se nomme {self.prenom}"
    
    def afficherAge(self):
        return f"L'animal a {self.age} ans"
    
    def vieillir(self):
        return "L'animal a", int(self.age) + 1, "ans"
    
animal = Animal(input("Entrez le nom de l'animal : "), input("Entrez l'âge de l'animal : "))
print("")
print(animal.nommer())
print(animal.afficherAge())
print(animal.vieillir())