from sys import path
import os

class TemperaturesCaptees:
    def __init__(self):
        self.id_capteur = 0
        self.temp_max = 0.0
        self.temp_min = 0.0
        self.temp_midi = 0.0
    
    def saisirTemperaturesCaptees(self):
        while True:
            try:
                self.id_capteur = int(input("Entrez l'identifiant du capteur : "))
                break
            except ValueError:
                print("Erreur : veuillez entrer un nombre entier valide")
        
        while True:
            try:
                self.temp_max = float(input("Entrez la température maximale (°C) : "))
                if self.temp_max < -50 or self.temp_max > 100:
                    print("Erreur : la température doit être entre -50°C et 100°C")
                    continue
                break
            except ValueError:
                print("Erreur : veuillez entrer un nombre valide")
        
        while True:
            try:
                self.temp_min = float(input("Entrez la température minimale (°C) : "))
                if self.temp_min < -50 or self.temp_min > 100:
                    print("Erreur : la température doit être entre -50°C et 100°C")
                    continue
                if self.temp_min > self.temp_max:
                    print("Erreur : la température minimale doit être inférieure ou égale à la température maximale")
                    continue
                break
            except ValueError:
                print("Erreur : veuillez entrer un nombre valide")
        
        while True:
            try:
                self.temp_midi = float(input("Entrez la température à midi (°C) : "))
                if self.temp_midi < -50 or self.temp_midi > 100:
                    print("Erreur : la température doit être entre -50°C et 100°C")
                    continue
                if self.temp_midi < self.temp_min or self.temp_midi > self.temp_max:
                    print("Erreur : la température à midi doit être entre la température minimale et la température maximale")
                    continue
                break
            except ValueError:
                print("Erreur : veuillez entrer un nombre valide")
        
        return self
    
    def ecartMaxTemperaturesCaptees(self):
        return abs(self.temp_max - self.temp_min)
    
    def afficheTemperaturesCaptees(self):
        ecart = self.ecartMaxTemperaturesCaptees()
        print(f"{self.id_capteur} * {self.temp_midi} * {self.temp_max} * {self.temp_min} * {ecart}")

class TemperaturesVille:
	def __init__(self):
		self.nom_ville = ""
		self.nb_capteurs = 0
		self.capteurs = []

	def saisirTemperaturesVille(self):
		self.nom_ville = input("Entrez le nom de la ville : ")
		while True:
			try:
				self.nb_capteurs = int(input("Entrez le nombre de capteurs (>=1) : "))
				if self.nb_capteurs < 1:
					print("Erreur : le nombre de capteurs doit être >= 1")
					continue
				break
			except ValueError:
				print("Erreur : veuillez entrer un nombre entier valide")
		self.capteurs = []
		for i in range(self.nb_capteurs):
			print(f"\nCapteur {i+1} :")
			capteur = TemperaturesCaptees()
			capteur.saisirTemperaturesCaptees()
			self.capteurs.append(capteur)
		return self

	def moyenneTemperatureAMidi(self):
		if not self.capteurs:
			return 0.0
		return sum(c.temp_midi for c in self.capteurs) / len(self.capteurs)

	def moyenneEcartMaxTemperature(self):
		if not self.capteurs:
			return 0.0
		return sum(c.ecartMaxTemperaturesCaptees() for c in self.capteurs) / len(self.capteurs)

	def afficheTemperaturesVille(self):
		moy_temp_midi = self.moyenneTemperatureAMidi()
		moy_ecart_max = self.moyenneEcartMaxTemperature()
		print(f"{self.nom_ville} - {self.nb_capteurs} - {moy_temp_midi} - {moy_ecart_max}")
		for capteur in self.capteurs:
			capteur.afficheTemperaturesCaptees()


if __name__ == "__main__":
	ville = TemperaturesVille()
	ville.saisirTemperaturesVille()
	ville.afficheTemperaturesVille()
