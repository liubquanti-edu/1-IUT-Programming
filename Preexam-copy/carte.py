class Carte:
    """Represente la carte reseau d'un PC."""

    def __init__(self, type_carte: str, mac: str, fabricant: str) -> None:
        self.type = type_carte
        self.mac = mac
        self.fabricant = fabricant

    @classmethod
    def saisir(cls) -> "Carte":
        """Construit une carte a partir des saisies utilisateur."""
        type_carte = input("Type de carte : ")
        mac = ""
        while not mac:
            mac = input("Adresse MAC : ")
        fabricant = input("Fabricant : ")
        return cls(type_carte, mac, fabricant)

    def to_text(self) -> str:
        """Chaine formatee pour l'affichage ou la sauvegarde."""
        return f"{self.type} | {self.mac} | {self.fabricant}"
