class Voiture:
    def __init__ (self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee

def afficher_details(self):
    print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}")

voiture1 = Voiture("Toyota", "Corolla", 2020)
afficher_details(voiture1)