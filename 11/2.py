class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __repr__(self):
        return f"Livre(titre={self.titre}, auteur={self.auteur})"
    
    def __str__(self):
        return f'"{self.titre}" de {self.auteur}'
    
l = Livre("1984", "George Orwell")

print(repr(l))