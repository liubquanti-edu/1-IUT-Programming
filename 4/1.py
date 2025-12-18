poids = int(input("Quel est le poids de votre lettre (en g) ? "))
if poids <= 20:
    tarif = 1.29
elif poids <= 100:
    tarif = 2.58
elif poids <= 250:
    tarif = 4.30
elif poids <= 500:
    tarif = 6.30
elif poids <= 1000:
    tarif = 7.70
elif poids <= 2000:
    tarif = 9.29
else:
    tarif = 0

if tarif > 0:
    print(f"Le tarif en lettre verte est de {tarif} €.")
else:
    print("Désolé, votre lettre est trop lourde.")