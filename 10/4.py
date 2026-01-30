class FibreOptique:
    def __init__(self, typeFibre, longueur, bandePassante, etat):
        self.typeFibre = typeFibre
        self.longueur = longueur
        self.bandePassante = bandePassante
        self.etat = etat
    
    def activer(self):
        if self.etat == "inactive":
            self.etat = "active"
    
    def desactiver(self):
        if self.etat == "active":
            self.etat = "inactive"
    
    def calculerTempsTransmission(self, volumeDonnees):
        tempsTrans = volumeDonnees / self.bandePassante
        return tempsTrans

fibre1 = FibreOptique("verre", 100, 10, "inactive")
fibre1.activer()

fibre2 = FibreOptique("plastique", 50, 5, "active")
tempsTrans = fibre2.calculerTempsTransmission(0.2)
print(f"Temps de transmission pour fibre2: {tempsTrans} s")
