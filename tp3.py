import random


def restart():
    recommence = input("voulez vous passer au prochain niveau")
    if recommence == "oui":
        return True
    elif recommence == "non":
        return False


hearts = 20
n_victoir = 0
win_streaks = 0
afficher_regle = False
force_de_monstre = 0

jouer = True
while jouer:
    if afficher_regle:
        afficher_regle = False
    else:
        if win_streaks == 3:
            force_de_monstre = random.randint(10, 18)
        else:
            force_de_monstre = random.randint(1, 6)

    chifre_du_dee_de_20 = random.randint(10, 20)
    if win_streaks <= 3:
        print(f"il y a un monstre avec difficulté de {force_de_monstre}")
    else:
        print(f"il y a un grand boss monstres avec difficulté de {force_de_monstre}")
    print("quesceque vous voulez faire")
    print("1-attaquer le monstre")
    print("2-contourner l'adversaire")
    print("3-afficher les regles")
    print("4-quiter le jeu")
    option = int(input("choisisser une des quartres options en inserant le nombre qui corespond: "))
    print()
    if option == 1:
        # different si boss
        if win_streaks == 3:
            chifredudee = random.randint(10, 20)
            print("voici un plus gros dee avec 20 face pour avoir une force d'attaque plus fort")
            win_streaks = 0
        else:
            chifredudee = random.randint(1, 6)
            print(f"vous roulez ler chiffre {chifredudee} ")

        if chifredudee >= force_de_monstre:
            hearts += force_de_monstre
            n_victoir += 1
            win_streaks += 1
            print("le monstre est mort bravo")
            print(f"il vous reste {hearts} de vie")
            print(f"vous avez {n_victoir} de victoir\n")
        elif chifredudee < force_de_monstre:
            hearts -= force_de_monstre
            win_streaks = 0
            print("vous avez perdu de la vie")
            print(f"il vous reste {hearts} de vie")
            print(f"vous avez {n_victoir} de victoir\n")
    elif option == 2:
        print()
        print("vous decider de contourner le monstre")
        print("pendant qu'il dors mais vous faite tomber une roche")
        print("lemonstre se reveille et vous attaque just qua votre mort")
        jouer = False
    elif option == 3:
        afficher_regle = True
        print()
        print("vous avec 20 point de vie\n ")
        print("si vous choisisser loption 1 vous aller rouler un dee\n")
        print("plus le chiffre est haut plus de dommage vous faite\n")
        print("le but est de tuer tout les monstre dans votre chemin\n")
    elif option == 4:
        print("c'est correct a la prochain fois.")
        jouer = False

    if hearts < 0:
        if not restart():
            jouer = False
