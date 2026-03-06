def triSallesNbpc(salles) :
    return sorted(salles, key=lambda salle: salle.nombre_pc)

def sauvegarderPCs(PCs) :
    with open("ordinateurs.txt", "w") as f :
        for pc in PCs :
            f.write(f"{pc.id} | {pc.taille_ecran}\" | {pc.ram} Go | {pc.carte.type} | {pc.carte.mac} | {pc.carte.fabricant}\n")

def sauvegarderSalles(salles) :
    with open("salles.txt", "w") as f :
        for salle in salles :
            f.write(f"Salle {salle.id} :\n")
            for pc in salle.liste_pc :
                f.write(f"{pc.id} | {pc.taille_ecran}\" | {pc.ram} Go | {pc.carte.type} | {pc.carte.mac} | {pc.carte.fabricant}\n")
