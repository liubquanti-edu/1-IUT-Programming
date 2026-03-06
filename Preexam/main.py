import saisir
import data

salles = []
for i in range(2):
    salles.append(saisir.saisirSalle())

PCs = [pc for salle in salles for pc in salle.liste_pc]

salles_tries = data.triSallesNbpc(salles)
data.sauvegarderPCs(PCs)
data.sauvegarderSalles(salles_tries)
