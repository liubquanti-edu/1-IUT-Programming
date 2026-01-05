string = input("Sailsir une chaine : ")

lettres = sum(c.isalpha() for c in string)
chiffres = sum(c.isdigit() for c in string)
symboles = len(string) - lettres - chiffres

print(f"Le nombre de lettres est {lettres}, le nombre de chiffres est {chiffres}, le nombre de symboles est {symboles}.")