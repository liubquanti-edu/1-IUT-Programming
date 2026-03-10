from carte import Carte


class PC:
    """Represente un poste informatique."""

    def __init__(self, identifiant: str, taille_ecran: int, ram: int, carte: Carte) -> None:
        self.id = identifiant
        self.taille_ecran = taille_ecran
        self.ram = ram
        self.carte = carte

    @classmethod
    def saisir(cls) -> "PC":
        """Construit un PC a partir des saisies utilisateur."""
        identifiant = ""
        while not identifiant:
            identifiant = input("ID du PC : ")
        taille_ecran = 0
        while taille_ecran <= 0:
            taille_ecran = int(input("Taille de l'ecran : "))
        ram = 0
        while ram <= 0:
            ram = int(input("Quantite de RAM : "))
        carte = Carte.saisir()
        return cls(identifiant, taille_ecran, ram, carte)

    def to_text(self) -> str:
        return f"{self.id} | {self.taille_ecran}\" | {self.ram} Go | {self.carte.to_text()}"
