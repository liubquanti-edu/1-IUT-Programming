class Produit:
    def __init__(self, nom, description, reference, prix, categorie):
        self.nom = nom
        self.description = description
        self.reference = reference
        self.prix = prix
        self.categorie = categorie

    def __str__(self):
        return f"{self.nom} ({self.reference}) - {self.prix}€"

class Magasin:
    def __init__(self, nom, localisation, nombre_employes):
        self.nom = nom
        self.localisation = localisation
        self.nombre_employes = nombre_employes
        self.produits = []

    def ajouterProduit(self, produit):
        self.produits.append(produit)

    def supprimerProduit(self, reference):
        for produit in self.produits:
            if produit.reference == reference:
                self.produits.remove(produit)
                break

    def valeur_totale(self):
        total = 0
        for produit in self.produits:
            total += produit.prix
        return total

    def afficher(self):
        print(f"Magasin: {self.nom}, Localisation: {self.localisation}, Employés: {self.nombre_employes}")
        print("Produits:")
        if not self.produits:
            print("  Aucun produit")
        for produit in self.produits:
            print(f"  - {produit}")
        print(f"Valeur totale des produits: {self.valeur_totale()}€")
        print("-" * 40)

def trierMagEmp(magasins):
    magasins.sort(key=lambda m: m.nombre_employes)

def trierMagVal(magasins):
    magasins.sort(key=lambda m: m.valeur_totale())



if __name__ == "__main__":
    
    p1 = Produit("Télévision", "TV 4K", "REF001", 800, "Image")
    p2 = Produit("Machine à laver", "7kg", "REF002", 500, "Électroménager")
    p3 = Produit("Micro-ondes", "800W", "REF003", 150, "Cuisine")
    
    m1 = Magasin("Magasin A", "Paris", 10)
    m2 = Magasin("Magasin B", "Lyon", 5)

    m1.ajouterProduit(p1)
    m1.ajouterProduit(p2)
    m2.ajouterProduit(p3)

    magasins = [m1, m2]

    print("=== Magasins avant tri ===")
    for m in magasins:
        m.afficher()
    
    trierMagEmp(magasins)
    print("\n=== Magasins triés par nombre d'employés ===")
    for m in magasins:
        m.afficher()
    
    trierMagVal(magasins)
    print("\n=== Magasins triés par valeur totale des produits ===")
    for m in magasins:
        m.afficher()
