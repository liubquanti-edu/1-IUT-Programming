from afficher import Afficheur
from data import DataService
from salle import Salle


def collecter_salles() -> list[Salle]:
    salles: list[Salle] = []
    continuer = "o"
    while continuer.lower() == "o":
        salles.append(Salle.saisir())
        continuer = input("Ajouter une autre salle ? (o/n) : ") or "n"
    return salles


def main() -> None:
    salles = collecter_salles()
    if not salles:
        print("Aucune salle saisie." )
        return

    print("\nRecapitulatif des salles saisies :")
    for salle in salles:
        Afficheur.afficher_salle(salle)

    pcs = [pc for salle in salles for pc in salle.pcs()]
    salles_triees = DataService.tri_salles_nb_pc(salles)
    DataService.sauvegarder_pcs(pcs)
    DataService.sauvegarder_salles(salles_triees)
    print("\nFichiers sauvegardes.")


if __name__ == "__main__":
    main()
