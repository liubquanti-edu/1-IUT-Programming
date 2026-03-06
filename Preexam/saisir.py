import carte
import pc
import salle

def saisirCarte() :
    type = input("Type de carte : ")
    mac = ""
    while mac == "" :
        mac = input("Adresse MAC : ")
    fabricant = input("Fabricant : ")
    return carte.carte(type, mac, fabricant)

def saisirPC() :
    id = ""
    while id == "" :
        id = input("ID du PC : ")
    taille_ecran = 0
    ram = 0
    while taille_ecran <= 0 :
        taille_ecran = int(input("Taille de l'écran : "))
    while ram <= 0 :
        ram = int(input("Quantité de RAM : "))
    carte = saisirCarte()
    return pc.pc(id, taille_ecran, ram, carte)

def saisirSalle() :
    id = ""
    while id == "" :
        id = input("ID de la salle : ")
    nombre_pc = 0
    while nombre_pc <= 0 :
        nombre_pc = int(input("Nombre de PC : "))
    liste_pc = []
    for i in range(nombre_pc) :
        print("Saisie du PC n°", i + 1)
        liste_pc.append(saisirPC())
    return salle.salle(id, nombre_pc, liste_pc)