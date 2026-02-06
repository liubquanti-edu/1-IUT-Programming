class Etudiant:
    def __init__(self):
        self.nom = ""
        self.prenom = ""
        self.ine = ""
        self.email = ""
        self.notes_coefficients = []
    
    def saisir(self):
        self.nom = input("Nom: ").strip()
        self.prenom = input("Prénom: ").strip()
        self.ine = input("INE: ").strip()
        self.email = input("Email: ").strip()
        
        self.notes_coefficients = []
        while True:
            try:
                note = float(input("Note (0-20) ou -1 pour arrêter: "))
                if note == -1:
                    break
                if not (0 <= note <= 20):
                    print("La note doit être entre 0 et 20")
                    continue
                
                coef = float(input("Coefficient (0.5-3): "))
                if not (0.5 <= coef <= 3):
                    print("Le coefficient doit être entre 0.5 et 3")
                    continue
                
                self.notes_coefficients.append([note, coef])
            except ValueError:
                print("Entrée invalide")
    
    def afficher(self):
        print("")
        print(f"Nom: {self.nom} {self.prenom}")
        print(f"INE: {self.ine}")
        print(f"Email: {self.email}")
        print(f"Notes et coefficients: {self.notes_coefficients}")
        print(f"Moyenne générale: {self.moyenne_generale():.2f}")
        print(f"Validation année: {'OUI' if self.valide_annee() else 'NON'}")
    
    def moyenne_generale(self):
        if not self.notes_coefficients:
            return 0
        
        somme_notes_coef = sum(note * coef for note, coef in self.notes_coefficients)
        somme_coef = sum(coef for note, coef in self.notes_coefficients)
        
        return somme_notes_coef / somme_coef if somme_coef > 0 else 0
    
    def valide_annee(self):
        if not self.notes_coefficients:
            return False
        
        moyenne = self.moyenne_generale()
        notes_min = min(note for note, coef in self.notes_coefficients)
        
        return moyenne >= 10 and notes_min >= 5
    
    def __lt__(self, other):
        return self.moyenne_generale() < other.moyenne_generale()


def afficher_etudiants_tries(etudiants):
    etudiants_tries = sorted(etudiants, reverse=True)
    print("")
    for etudiant in etudiants_tries:
        etudiant.afficher()


if __name__ == "__main__":
    etudiants = []
    
    while True:
        print("\n1. Ajouter un étudiant")
        print("2. Afficher les étudiants triés")
        print("3. Quitter")
        choix = input("Choix: ").strip()
        
        if choix == "1":
            etudiant = Etudiant()
            etudiant.saisir()
            etudiants.append(etudiant)
        elif choix == "2":
            afficher_etudiants_tries(etudiants)
        elif choix == "3":
            break
        else:
            print("Choix invalide")
