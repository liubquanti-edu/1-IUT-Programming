chaine1 = input("Saisir la première chaine: ")
chaine2 = input("Saisir la deuxième chaine: ")

milieu = len(chaine1) // 2

nouvelle_chaine = chaine1[:milieu] + chaine2 + chaine1[milieu:]

print(f"Les chaines originales sont \"{chaine1}\" et \"{chaine2}\"")
print(f"Après l'ajout de la deuxième chaine au milieu, on a : \"{nouvelle_chaine}\"")