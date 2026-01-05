def afficher_plateau(plateau):
    print("    A   B   C")
    print("  ╔═══╦═══╦═══╗")
    for i in range(3):
        ligne = f"{i + 1} ║"
        for j in range(3):
            ligne += f" {plateau[i][j][0] or ' '} ║"
        print(ligne)
        if i < 2:
            print("  ╠═══╬═══╬═══╣")
        else:
            print("  ╚═══╩═══╩═══╝")


def verifier_victoire(plateau, joueur):
    symbole = "X" if joueur == 1 else "O"
    for i in range(3):
        if all(plateau[i][j][0] == symbole for j in range(3)) or \
           all(plateau[j][i][0] == symbole for j in range(3)):
            return True
    if all(plateau[i][i][0] == symbole for i in range(3)) or \
       all(plateau[i][2 - i][0] == symbole for i in range(3)):
        return True
    return False


def jeu_morpion():
    plateau = [[[None, None, False] for _ in range(3)] for _ in range(3)]
    joueur = 1
    tour = 0

    while tour < 9:
        afficher_plateau(plateau)
        case_valide = False

        while not case_valide:
            choix = input(f"Joueur{joueur}, quelle case (ex B2) ? ").strip().upper()
            if len(choix) == 2 and choix[0] in "ABC" and choix[1] in "123":
                col = ord(choix[0]) - ord('A')
                row = int(choix[1]) - 1
                if not plateau[row][col][2]:
                    plateau[row][col] = ["X" if joueur == 1 else "O", joueur, True]
                    case_valide = True
                else:
                    print("Il existe déjà un pion à cette adresse.")
            else:
                print("Erreur de saisie, saisir une lettre entre A et C et un chiffre entre 1 et 3.")

        if verifier_victoire(plateau, joueur):
            afficher_plateau(plateau)
            print(f"Joueur{joueur} a gagné !")
            return

        joueur = 2 if joueur == 1 else 1
        tour += 1

    afficher_plateau(plateau)
    print("Égalité entre les deux joueurs.")


jeu_morpion()