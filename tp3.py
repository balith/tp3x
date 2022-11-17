import random


def restart():
    recommence = input("voulez vous passer au prochain niveau")
    if recommence == "oui":
        return True
    elif recommence == "non":
        return False


hearts = 20

jouer = True
while jouer:

    forcedemonstre = random.randint(1, 6)
    forcedugrandmonstre = random.randint(10, 20)
    print("")

    print(f"il y a un grand monstre avec difficulté de {forcedemonstre}")
    print("quesceque vous voulez faire")
    print("1-attaquer le monstre")
    print("2-contourner l'adversaire")
    print("3-afficher les regles")
    print("4-quiter le jeu")
    option = int(input("choisisser une des quartres options en inserant le nombre qui corespond: "))
    print()

    if option == 1:
        chifredudee = random.randint(1, 6)

        print(f"vous roulez ler chiffre {chifredudee} ")

        if chifredudee > forcedemonstre:
            print("le monstre est mort bravo")
            print(f"il vous reste {hearts + forcedemonstre} de vie")
        elif chifredudee < forcedemonstre:
            print("vous avez perdu de la vie")
            print(f"il vous reste {hearts - forcedemonstre} de vie")
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

    if jouer < 3:
        chifredudeede20 = random.randint(10, 25)

        print(f"vous roulez ler chiffre {chifredudeede20} ")

        if chifredudeede20 > forcedugrandmonstre:
            print("le monstre est mort bravo")
            print(f"il vous reste {hearts + forcedugrandmonstre} de vie")
        elif chifredudeede20 < forcedugrandmonstre:
            print("vous avez perdu tout votre vie")
            print(f"il vous reste {hearts - forcedugrandmonstre} de vie")
    if hearts < 0:
        if not restart():
            jouer = False
