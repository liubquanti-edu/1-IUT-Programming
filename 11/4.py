class Serveur:
	def __init__(self, nom, adresse_ip, capacite_stockage, etat="éteint"):
		self.nom = nom
		self.adresse_ip = adresse_ip
		self.capacite_stockage = capacite_stockage
		self.etat = etat

	def allumer(self):
		if self.etat == "éteint":
			self.etat = "allumé"
			print(f"{self.nom} est maintenant allumé.")
		else:
			print(f"{self.nom} est déjà allumé.")

	def eteindre(self):
		if self.etat == "allumé":
			self.etat = "éteint"
			print(f"{self.nom} est maintenant éteint.")
		else:
			print(f"{self.nom} est déjà éteint.")

	def transmettre_donnees(self, volume_donnees, debit_reseau):
		temps = (volume_donnees * 8) / debit_reseau
		return temps

	def __lt__(self, other):
		return self.capacite_stockage < other.capacite_stockage

	def __gt__(self, other):
		return self.capacite_stockage > other.capacite_stockage

	def __eq__(self, other):
		return self.capacite_stockage == other.capacite_stockage

if __name__ == "__main__":
	serveur1 = Serveur("Serveur-A", "192.168.1.1", 10)
	serveur1.allumer()
	print(f"Etat de {serveur1.nom} : {serveur1.etat}")

	serveur2 = Serveur("Serveur-B", "192.168.1.2", 5)
	temps = serveur2.transmettre_donnees(50, 10)
	print(f"Temps de transmission de 50 Go via {serveur2.nom} : {temps:.2f} secondes.")

	if serveur1 > serveur2:
		print(f"{serveur1.nom} a une plus grande capacité de stockage ({serveur1.capacite_stockage} To")
	elif serveur2 > serveur1:
		print(f"{serveur2.nom} a une plus grande capacité de stockage ({serveur2.capacite_stockage} To")
	else:
		print(f"{serveur1.nom} et {serveur2.nom} ont la même capacité de stockage ({serveur1.capacite_stockage} To).")