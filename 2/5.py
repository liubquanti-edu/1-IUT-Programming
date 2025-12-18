prixHT = float(input("Prix HT (en euro) "))

tauxTVA = float(input("Taux TVA (en %) : "))

prixTTC = prixHT * (1 + tauxTVA / 100)

print(f"Prix TTC : {round(prixTTC, 2)} euro")