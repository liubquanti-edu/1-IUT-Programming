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

    def __lt__(self, other):
        return self.bandePassante < other.bandePassante

    def __eq__(self, other):
        return self.bandePassante == other.bandePassante

fibre1 = FibreOptique("verre", 100, 10, "inactive")
fibre2 = FibreOptique("plastique", 50, 5, "active")

if fibre1 > fibre2:
    print("Fibre1 a la plus grande bande passante.")
elif fibre1 < fibre2:
    print("Fibre2 a la plus grande bande passante.")
else:
    print("Les deux fibres ont la même bande passante.")
