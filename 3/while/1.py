bInf = int(input("Saisir un premire entier : "))
bSup = int(input("Saisir un second entier plus grand que le premier : "))

while bSup <= bInf:
    bSup = int(input("Erreur de saisie, recommencer : "))

print(f"{bInf} est bien > {bSup}")