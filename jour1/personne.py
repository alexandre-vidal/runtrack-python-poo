class Personne:
    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom
        
    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"
    
p1 = Personne("John", "Doe")
p2 = Personne("Jean", "Dupond")

print(p1.SePresenter())
print(p2.SePresenter())