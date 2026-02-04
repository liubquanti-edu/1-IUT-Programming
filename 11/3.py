class Etudiant:
	def __init__(self, ine: str, nom: str, prenom: str, age: int, annee_naissance: int) -> None:
		self.ine = ine
		self.nom = nom
		self.prenom = prenom
		self.age = age
		self.annee_naissance = annee_naissance

	def MemeNom(self, autre: "Etudiant") -> bool:
		return self.nom.lower() == autre.nom.lower()

	def PlusAgee(self, autre: "Etudiant") -> "Etudiant":
		if self.annee_naissance < autre.annee_naissance:
			return self
		if self.annee_naissance > autre.annee_naissance:
			return autre
		return self if self.age >= autre.age else autre


if __name__ == "__main__":
	etudiant_un = Etudiant("123456", "Dupont", "Alice", 20, 2005)
	etudiant_deux = Etudiant("654321", "dupont", "Bob", 22, 2003)

	meme_nom = etudiant_un.MemeNom(etudiant_deux)
	plus_age = etudiant_un.PlusAgee(etudiant_deux)

	print("Meme nom de famille:", meme_nom)
	print("Plus age:", f"{plus_age.prenom} {plus_age.nom}")
