def afficherPC(pc) :
    print(f"{pc.id} | {pc.taille_ecran}\" | {pc.ram} Go | {pc.carte.type} | {pc.carte.mac} | {pc.carte.fabricant}")

def afficherSalle(salle) :
    print(f"Salle {salle.id} :")
    for pc in salle.liste_pc :
        afficherPC(pc)

