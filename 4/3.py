annee = int(input("Quelle année ? "))
if (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0):
    print("L'année", annee, "est bissextile.")
else:
    print("L'année", annee, "n'est pas bissextile.")