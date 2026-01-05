def obtenirMots(chaine):
    return chaine.replace("\n", "").split()

def compterMots(liste_mots):
    return len(liste_mots)

def motPlusLong(liste_mots):
    return max(liste_mots, key=len)

citations = (
    "And we danced, on the brink of an unknown future, to an echo from a vanished past. (John Wyndham) \n"
    "Life is what happens to you while you're busy making other plans. (wrongly attributed to John Lennon) \n"
    "You cannot overestimate the unimportance of practically everything. (John Maxwell)"
)

liste_citations = citations.splitlines()

for citation in liste_citations:
    mots = obtenirMots(citation)
    nombre_mots = compterMots(mots)
    mot_le_plus_long = motPlusLong(mots)
    print(f"Citation: {citation}")
    print(f"Nombre de mots: {nombre_mots}, Le mot le plus long: {mot_le_plus_long}\n")