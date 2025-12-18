jour = int(input("Saisir le numéro de jour dans le mois : "))
mois = int(input("Saisir le numéro de mois : "))
annee = int(input("Saisir l'année : "))

print(f"Nous sommes le {jour}/{mois}/{annee}")

if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    bissextile = True
else:
    bissextile = False

if mois in [1, 3, 5, 7, 8, 10, 12]:
    jours = 31
elif mois in [4, 6, 9, 11]:
    jours = 30
elif mois == 2:
    if bissextile:
        jours = 29
    else:
        jours = 28

if jour < jours:
    jour += 1
else:
    jour = 1
    if mois < 12:
        mois += 1
    else:
        mois = 1
        annee += 1

print(f"Demain nous serons le {jour}/{mois}/{annee}")