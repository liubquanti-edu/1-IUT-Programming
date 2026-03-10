from salle import Salle


class Afficheur:
    @staticmethod
    def afficher_pc(pc) -> None:
        print(pc.to_text())

    @staticmethod
    def afficher_salle(salle: Salle) -> None:
        print(f"Salle {salle.id} ({salle.nombre_pc} PC)")
        for pc in salle.liste_pc:
            Afficheur.afficher_pc(pc)
