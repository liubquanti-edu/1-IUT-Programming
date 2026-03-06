THEMATIQUES = {
	1: "Science",
	2: "Littérature",
	3: "Histoire",
	4: "Oeuvre étrangère",
	5: "Divers"
}

class Livre:
	def __init__(self, titre, thematique, nb_pages):
		self.titre = titre
		self.thematique = thematique
		self.nb_pages = nb_pages

class CollectionThematique:
    def __init__(self, thematique: int, livres: list[Livre] = None):
        self.thematique = thematique
        self.livres = livres if livres is not None else []
        self.nb_livres = len(self.livres)

    def ajouter_livre(self, livre: Livre):
        if livre.thematique == self.thematique:
            self.livres.append(livre)
            self.nb_livres = len(self.livres)
        else:
            raise ValueError("Le livre n'appartient pas à cette thématique.")

def saisirLivre():
	while True:
		titre = input("Titre du livre : ").strip()
		if titre:
			break
		print("Le titre ne doit pas être vide.")
	while True:
		try:
			nb_pages = int(input("Nombre de pages : "))
			if nb_pages > 0:
				break
		except:
			pass
		print("Le nombre de pages doit être un entier positif.")
	while True:
		print("Choisissez la thématique :")
		for k, v in THEMATIQUES.items():
			print(f"{k}. {v}")
		try:
			thematique = int(input("Votre choix : "))
			if thematique in THEMATIQUES:
				break
		except:
			pass
		print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
	return Livre(titre, thematique, nb_pages)

def afficheLivre(livre):
	print(f"{livre.titre} : {THEMATIQUES[livre.thematique]}, {livre.nb_pages}")

def saisirCollectionThematique():
    print("Choisissez la thématique de la collection :")
    for k, v in THEMATIQUES.items():
        print(f"{k}. {v}")
    while True:
        try:
            thematique = int(input("Votre choix : "))
            if thematique in THEMATIQUES:
                break
        except:
            pass
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 5.")
    collection = CollectionThematique(thematique)
    while True:
        print("\nAjout d'un livre à la collection :")
        livre = saisirLivre()
        try:
            collection.ajouter_livre(livre)
        except ValueError:
            print("Le livre n'appartient pas à la thématique de la collection. Il ne sera pas ajouté.")
        continuer = input("Voulez-vous ajouter un autre livre ? (o/n) : ").strip().lower()
        if continuer == 'n':
            break
    return collection

# livre = saisirLivre()
# afficheLivre(livre)
collection = saisirCollectionThematique()
print(f"Collection de thématique {THEMATIQUES[collection.thematique]} : {collection.nb_livres} livres")