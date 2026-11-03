import os


def ClearCmd():
    """
    Cette fonction s'occupe uniquement de clear le Terminal afin d'avoir un interface plus propre sans tout l'historique juste au dessus.
    """
    os.system('cls' if os.name == 'nt' else 'clear')



def Affichage(grille):
    """
    Cette fonction s'occupe d'afficher la grille de morpion de manière propre et esthétique.
    """
    print("\n     A    B    C")
    print("    ┌───┬───┬───┐")
    print(f" 1  │ {grille[0][0]} │ {grille[0][1]} │ {grille[0][2]} │")
    print("    ├───┼───┼───┤")
    print(f" 2  │ {grille[1][0]} │ {grille[1][1]} │ {grille[1][2]} │")
    print("    ├───┼───┼───┤")
    print(f" 3  │ {grille[2][0]} │ {grille[2][1]} │ {grille[2][2]} │")
    print("    └───┴───┴───┘")



def morpion():
    """
    La fonction qui exécute tout et s'occupe de placer les choix dans la grille pour faire tourner le morpion.
    """
    ClearCmd()
    grille=[[" "," "," "],[" "," "," "],[" "," "," "]]
    joueur_1=input("\nSélectionner le pseudo pour le joueur 1 : ")
    joueur_2=input("\nSélectionner le pseudo pour le joueur 2 : ")
    ClearCmd()
    Affichage(grille)
    while True:
        print("\nc'est au tour de",joueur_1,":\n")
        ligne, colonne = Selection(grille)
        grille[ligne][colonne]="X"
        ClearCmd()
        Affichage(grille)
        win = VerifWin(grille)
        if win == "X":
            print(joueur_1,"a gagné")
            break
        if VerifNul(grille)==True:
            print("Match NUL personne ne gagne.")
            break
        print("\nc'est au tour de",joueur_2,":\n")
        ligne, colonne = Selection(grille)
        grille[ligne][colonne]="O"
        ClearCmd()
        Affichage(grille)
        win = VerifWin(grille)
        if win == "O":
            print(joueur_2,"a gagné")
            break
        


def Selection(grille):
    """
    Cette fonction s'occupe de la gestion de la sélection de la case pour jouer,
    elle vérifie que la case est existante et aussi qu'elle n'est pas déja utlisé.
    """
    colonnetrue = False
    lignetrue = False
    while True:
        colonne=input("Sélectionner la colonne où placer votre pion : ")
        ligne=input("sélectionner la ligne où placer votre pion : ")
        if colonne=="A" or colonne=="a":
            colonne=0
            colonnetrue = True
        elif colonne=="B" or colonne=="b":
                colonne=1
                colonnetrue=True
        elif colonne=="C" or colonne=="c":
                colonne=2
                colonnetrue = True
        else:
            print(" Erreur : Vous avez mal saisi la colonne.")
            colonnetrue=False
        if ligne=="1":
            ligne = 0
            lignetrue=True
        elif ligne=="2":
            ligne = 1
            lignetrue=True
        elif ligne == "3":
            ligne = 2
            lignetrue=True
        else :
            print("Erreur : Vous avez mal saisi la ligne.")
            lignetrue=False
        if colonnetrue== True and lignetrue==True:
            if grille[ligne][colonne]!=" ":
                print("\nCase déja prise.\n")
            else :
                break
    return ligne, colonne



def VerifWin(grille):
    """
    Cette fonction s'occupe de vérifier si un utilisateur a gagné,
    en vérifiant si il a un meme symbole sur la meme ligne/colonne/diagonale.
    """
    for a in range(3):
        if grille[0][a]==grille[1][a] and grille[0][a]==grille[2][a]:
            if grille[0][a]=="X":
                return "X"
            elif grille[0][a]=="O":
                return "O"
        if grille[a][0]==grille[a][1] and grille[a][0]==grille[a][2]:
            if grille[a][0]=="X":
                return "X"
            elif grille[a][0]=="O":
                return "O"
    if grille[0][0]==grille[1][1] and grille[0][0]==grille[2][2]:
        if grille[0][0]=="X":
            return "X"
        elif grille[0][0]=="O":
            return "O"
    if grille[2][0]==grille[1][1] and grille[2][0]==grille[0][2]:
        if grille[1][1]=="X":
            return "X"
        elif grille[1][1]=="O":
            return "O"



def VerifNul(grille):
    """
    Vérifie si la grille est pleine pour déclarer partie nul.
    """
    for a in range(3):
        for b in range(3):
            if grille[a][b]==" ":
                return False
    return True



morpion()