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

if __name__ == "__main__":
    
    TemperaturesCaptees1 = TemperaturesCaptees()
    TemperaturesCaptees1.saisirTemperaturesCaptees()
    
    ecart = TemperaturesCaptees1.ecartMaxTemperaturesCaptees()
    print(f"Écart maximum : {ecart}°C")
    
    TemperaturesCaptees1.afficheTemperaturesCaptees()
