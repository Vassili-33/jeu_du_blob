"""affichage sur le terminal du jeu"""

def affiche_case(case):
    """case est un entier égal a -i si prise par le joueur i, égal au numéro de la case sinon"""

    if case == -1:
        print("🔵",end =" ")

    elif  case == -2:
        print("🔴", end = " ")

    else:
        print(str (case))


def affiche_plateau(plateau):
    """affiche l'état du plateau dans le terminal"""
    for ligne in plateau:
        for case in ligne:
            affiche_case(case)
        print()

def affiche_coup_invalide():
    """"affiche que le coup est invalide"""

    print("coup invalide")
