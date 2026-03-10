from pc import PC
from salle import Salle


class DataService:
    """Centralise les traitements sur les salles et les PC."""

    @staticmethod
    def tri_salles_nb_pc(salles: list[Salle]) -> list[Salle]:
        return sorted(salles, key=lambda salle: salle.nombre_pc)

    @staticmethod
    def sauvegarder_pcs(pcs: list[PC], chemin: str = "ordinateurs.txt") -> None:
        with open(chemin, "w", encoding="utf-8") as fichier:
            for pc in pcs:
                fichier.write(pc.to_text() + "\n")

    @staticmethod
    def sauvegarder_salles(salles: list[Salle], chemin: str = "salles.txt") -> None:
        with open(chemin, "w", encoding="utf-8") as fichier:
            for salle in salles:
                fichier.write(salle.to_text() + "\n")
