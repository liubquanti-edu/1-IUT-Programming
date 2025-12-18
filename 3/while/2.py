r = input("Saisir 'oui' ou 'non' : ")

while r != "oui" and r != "non":
	r = input("Erreur de saisie, recommencer : ")
	
print(f"Vous avez repondu {r}")