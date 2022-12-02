import random


def restart():
    recommence = input("voulez vous passer au prochain niveau")
    if recommence == "oui":
        return True
    elif recommence == "non":
        return False


hearts = 20
n_victoir = 0
jouer = True
while jouer:
    if n_victoir < 3:
        force_du_grand_monstre = random.randint(10, 20)
        if chifre_du_dee_de_20 > force_du_grand_monstre:
            chifre_du_dee_de_20 = random.randint(10, 20)
            print("voici un plus gros dee avec 20 face pour avoir une force d'attaque plus fort")
            print(f"vous roulez ler chiffre {chifre_du_dee_de_20} ")
            print("le monstre est mort bravo")
            print(f"il vous reste {hearts + force_du_grand_monstre} de vie")
            print(f"vous avez {n_victoir} de victoire")
        elif chifre_du_dee_de_20 < force_du_grand_monstre:
            print("vous avez perdu tout votre vie")
            print(f"il vous reste {hearts - force_du_grand_monstre} de vie")
            print(f"vous avez {n_victoir} de victoir")
    """
    si victoire == 3
        generer monstre boss (3-5)
        afficher info en fonction du type de monstre    
    sinon
        generer monstre normal (1-5)
        afficher info en fonction du type de monstre
    """
    force_de_monstre = random.randint(1, 6)
    print("")
    if n_victoir <= 3:
        print(f"il y a un grand boss monstre avec difficulté de {force_de_monstre}")
        print(f"il y a un grand boss monstres avec difficulté de {force_de_monstre}")
        print("quesceque vous voulez faire")
        print("1-attaquer le monstre")
        print("2-contourner l'adversaire")
        print("3-afficher les regles")
        print("4-quiter le jeu")
    elif
        print(f"il y a un monstre avec difficulté de {force_de_monstre}")
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
        chifredudee = random.randint(1, 6)
        chifre_du_dee_de_20 = random.randint(10, 20)

        print(f"vous roulez ler chiffre {chifredudee} ")

        if chifredudee >= force_de_monstre:
            hearts += force_de_monstre
            n_victoir += 1
            print("le monstre est mort bravo")
            print(f"il vous reste {hearts} de vie")
            print(f"vous avez {n_victoir} de victoir")
        elif chifredudee < force_de_monstre:
            hearts -= force_de_monstre
            print("vous avez perdu de la vie")
            print(f"il vous reste {hearts} de vie")
            print(f"vous avez {n_victoir} de victoir")
        # if n_victoir < 3:
        #     force_du_grand_monstre = random.randint(10, 20)
        #     chifre_du_dee_de_20 = random.randint(10, 20)
        #     print("voici un plus gros dee avec 20 face pour avoir une force d'attaque plus fort")
        #     print(f"vous roulez ler chiffre {chifre_du_dee_de_20} ")
        #
        #     if chifre_du_dee_de_20 > force_du_grand_monstre:
        #         print("le monstre est mort bravo")
        #         print(f"il vous reste {hearts + force_du_grand_monstre} de vie")
        #         print(f"vous avez {n_victoir} de victoir")
        #     elif chifre_du_dee_de_20 < force_du_grand_monstre:
        #         print("vous avez perdu tout votre vie")
        #         print(f"il vous reste {hearts - force_du_grand_monstre} de vie")
        #         print(f"vous avez {n_victoir} de victoir")
    elif option == 2:
        print()
        print("vous decider de contourner le monstre")
        print("pendant qu'il dors mais vous faite tomber une roche")
        print("lemonstre se reveille et vous attaque just qua votre mort")
        jouer = False
    elif option == 3:
        print()
        print("vous avec 20 point de vie ")
        print("si vous choisisser loption 1 vous aller rouler un dee")
        print("plus le chiffre est haut plus de dommage vous faite")
        print("le but est de tuer tout les monstre dans votre chemin")
    elif option == 4:
        print("c'est correct a la prochain fois.")
        jouer = False

    if hearts < 0:
        if not restart():
            jouer = False