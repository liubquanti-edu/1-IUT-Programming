nombre_de_fruits = int(input("Combien de fruits ? "))

liste_de_fruits = []

for _ in range(nombre_de_fruits):
    fruit = input("Saisir un fruit : ")
    liste_de_fruits.append(fruit)

liste_de_fruits.sort()

print(liste_de_fruits)