from typing import List

from pc import PC


class Salle:
    """Regroupe un ensemble de PC de maniere oriente objet."""

    def __init__(self, identifiant: str) -> None:
        self.id = identifiant
        self.liste_pc: List[PC] = []

    @property
    def nombre_pc(self) -> int:
        return len(self.liste_pc)

    @classmethod
    def saisir(cls) -> "Salle":
        identifiant = ""
        while not identifiant:
            identifiant = input("ID de la salle : ")
        salle = cls(identifiant)
        nb_pc = 0
        while nb_pc <= 0:
            nb_pc = int(input("Nombre de PC : "))
        for index in range(nb_pc):
            print(f"Saisie du PC #{index + 1}")
            salle.ajouter_pc(PC.saisir())
        return salle

    def ajouter_pc(self, pc: PC) -> None:
        self.liste_pc.append(pc)

    def nb_pc_cisco(self) -> int:
        return sum(1 for pc in self.liste_pc if pc.carte.fabricant.lower() == "cisco")

    def memoire_minimale(self) -> int:
        if not self.liste_pc:
            return 0
        return min(pc.ram for pc in self.liste_pc)

    def pcs(self) -> List[PC]:
        return list(self.liste_pc)

    def to_text(self) -> str:
        lignes = [f"Salle {self.id} :"]
        lignes.extend(pc.to_text() for pc in self.liste_pc)
        return "\n".join(lignes)
