def nbPcCisco(salle) :
    count = 0
    for pc in salle.liste_pc :
        if pc.carte.fabricant == "Cisco" :
            count += 1
    return count

def memoireMinimale(salle) :
    min_ram = salle.liste_pc[0].ram
    for pc in salle.liste_pc :
        if pc.ram < min_ram :
            min_ram = pc.ram
    return min_ram