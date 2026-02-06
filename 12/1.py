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
fibre3 = FibreOptique("verre", 75, 15, "active")
fibre4 = FibreOptique("plastique", 60, 8, "inactive")

fibres = [fibre1, fibre2, fibre3, fibre4]

fibres_triees_lt = sorted(fibres)
for fibre in fibres_triees_lt:
    print(f"  Type: {fibre.typeFibre}, Bande passante: {fibre.bandePassante}")

fibres_triees_key = sorted(fibres, key=lambda f: f.bandePassante)
print("")
for fibre in fibres_triees_key:
    print(f"  Type: {fibre.typeFibre}, Bande passante: {fibre.bandePassante}")
