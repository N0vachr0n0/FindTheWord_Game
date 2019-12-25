"""
NOM DU PROJET: FIND TH3 WORD

CREATE BY: N0vachr0n0

VERSION: 1.2

"""

import random
import os
import time


def menu():
    print("\n\t\t***********************************")
    print("\t\t**********FIND TH3 WORD ***********")
    print("\t\t***********************************")

    print("\n\n\t\tBIENVENU DANS FIND TH3 WORD !!\n")
    print("\n\t\t--------MENU PRINCIPAL--------\n")

    print("1 -> JOUER \n2 -> COMMENT JOUER ? \n3 -> MEILLEUR SCORE \n4 -> DEMO\n5 -> SORTIR\n")
    print("Credit : NI NO KATA\n")
    choix = input("Entrez Votre Choix Svp = ")
    choix = int(choix)

    return choix


def Msg(a):
    if a == 1:
        print("\nFélicitations vous avez trouvé le Mot correct !!!\n")
    if a == 2:
        print("\nDésolé Mot incorrect !! Courage à vous, veillez réessayer.\n")
    if a == 3:
        print("\nGAME OVER PARTIE TERMINEE !\n Vous n'avez plus de vie restante !\n")


def ChoixLvl():
    error = True
    while error == True:
        print("\nCHOISISSEZ LE NIVEAU !\n")
        print("1 -> FACILE")
        print("2 -> MOYEN")
        print("3 -> DIFFICILE")

        lvl = input("\nENTREZ LE NIVEAU SVP = ")
        lvl = int(lvl)

        if lvl > 3 or lvl < 1:
            print("\nChoix incorrect\n")
        else:
            error = False

    return lvl


def Msglvl(lvl):
    if lvl == 1:
        print("\nOh !! Oh ! Oh !!! Vous avez Choisi le niveau FACILE !\nDans ce Mode "
              "vous serez confronter à des mots de 4 lettres\n\n")
    if lvl == 2:
        print("\nOh !! Oh ! Oh !!! Vous avez Choisi le niveau MOYEN !\nDans ce Mode "
              "vous serez confronter à des mots de 5 à 7 lettres\n\n")
    if lvl == 3:
        print("\nOh !! Oh ! Oh !!! Vous avez Choisi le niveau DIFFICILE !\nDans ce Mode "
              "vous serez confronter à des mots de plus de 7 lettres\n\n")

    print("\t\t***INFOS***\nSi Votre nombre de vie restante atteint zéro (0) vous perdez la partie.")
    choixM = input("Appuyer ENTRER pour continuer...")
    return choixM


def Inside(score, vie, X):
    print("\nScore = %i" % (score))
    print("Vie restante = %i \n" % (vie))
    print("Voici Une Suite De Lettre : %s" % (X))
    print("\nA Quel Mot correspond il ?\n\n")
    rep = input("Reponse = ")

    return rep


def Howto():
    print("\nFIND TH3 WORD est un jeu dans lequel le joueur aura pour objectif de trouver le Mot correct grâce\n"
          "à la suite de lettre qu'il aura reçu.")
    print("\n\nLet's enjoy !!!")
    choixH = input("\nAppuyer entrer pour revenir au menu principal")

    return choixH


def GenerationWord(lvl):
    # global file_word
    check = []
    mot = ['data/word_lvl1', 'data/word_lvl2', 'data/word_lvl3']
    if lvl == 1:
        file_word = open(mot[lvl - 1], 'r')
    elif lvl == 2:
        file_word = open(mot[lvl - 1], 'r')
    elif lvl == 3:
        file_word = open(mot[lvl - 1], 'r')

    word = file_word.readlines()

    nbr_mot = 0
    for _ in word:
        nbr_mot += 1

        for _ in range(1000):  # Pour eviter la repetition de y
            y = random.randint(0, nbr_mot - 1)
            if y in check:
                continue
            else:
                check.append(y)
                break

        Initword = word[y]  # Transfert du mot corr

    return Initword


def Record_score_name(score, player):
    # ###Traitement du score puis stockage

    with open('data/dat_2', 'r') as file3:
        score_part2 = file3.readlines()
    high_score = score_part2[0]  # 0 = Niv facile / 1 = Niv moyen / 2 = Niv diff
    high_score = int(high_score)

    # score = 35

    if high_score < score:
        high_score = score
        # ###Sauvegarde du nom du joueur

        with open('data/dat_3', 'r') as file2:
            best_player = file2.readlines()
            best_player[0] = player + '\n'  # 0 = Niv facile / 1 = Niv moyen / 2 = Niv diff

        with open('data/dat_3', 'w') as file:
            file.writelines(best_player)

        temp = open('data/dat_3', 'w')
        temp.writelines(best_player)

        file2.close()
        file.close()

    high_score = str(high_score) + '\n'
    score_part2[0] = high_score

    temporaire = open('data/dat_2', 'w')

    temporaire.writelines(score_part2)  # MAJ du fichier score
    temporaire.close()


def playing(life, level):
    Vie0 = life
    Score = 0
    # check = []
    while Vie0 != 0:

        Initword = GenerationWord(level)  # Initword == Mot initial
        Initword = Initword.rstrip()  # Enlève \n

        InitwordMod = list(Initword)  # list != str
        random.shuffle(InitwordMod)  # permute les lettres de InitwordMod / il ne permute que les list
        wordX = "".join(InitwordMod)

        wordX = str(wordX)  # wordX redevient une str pour pouvoir le comparer à Initword
        Initword = str(Initword)
        os.system('clear')
        rep = Inside(score=Score, vie=Vie0, X=wordX)

        if rep == Initword:
            print("\nFélicitation ! Mot correct !\n")
            Score += 1
            time.sleep(2)

            continue
        elif rep != Initword:
            print("\nDommage !! Mot incorrect\n")
            Vie0 -= 1
            time.sleep(2)
            if Vie0 == 0:
                print("\nGAME OVER !! Vous n'avez plus de vie restante !\n")
                Record_score_name(Score, player)  # Enregistrement du score
                rep = input("Appuyer ENTRER pour revenir au menu principal.\n")

                if rep is not None:
                    break
            continue


# DEBUT MAIN PROGRAM --------------------------------
while True:

    choix = menu()
    if choix == 1:

        os.system('clear')
        player = input("Entrez votre nom svp : ")

        os.system('clear')
        lvl = ChoixLvl()
        choixM = Msglvl(lvl)

        if (choixM != None) and (lvl == 1):
            playing(4, lvl)

        elif (lvl == 2):
            playing(5, lvl)

        elif (lvl == 3):
            playing(6, lvl)
    # ---------------------------------------FIN CHOIX LVL------------------------------------------------

    elif choix == 2:

        os.system('clear')
        choixH = Howto()

        if choix != None:
            continue

    elif choix == 3:  # Best score

        os.system('clear')
        # Affichage des meilleurs scores
        with open('data/dat_2', 'r') as file:
            score_part2 = file.readlines()
        with open('data/dat', 'r') as file2:
            score_part1 = file2.readlines()
        with open('data/dat_3', 'r') as file2:
            best_player = file2.readlines()

        print(score_part1[0])  # titre
        for i in range(3):
            # i = 0
            print(score_part1[i + 3] + " " + "| " + "Nom = " + best_player[i] + " | " + "Score = " + score_part2[
                i] + "\n")
            # i+1 à cause du titre "meilleur score "
        rep = input("Entrez 1 pour revenir au menu principal.")
        if rep != None:
            continue


    elif choix == 4:
        # DEMO

        os.system('clear')
        word = ["visages", "visait", "visage", " tortionnaire", " tortue", "ambitieusement", "extérieur",
                "tortiller", "extérieure", "visa", "ambitieux"]

        Vie0 = 3
        Score = 0
        check = []

        while Vie0 != 0:

            for _ in range(1000):  # Pour eviter la repetition de y
                y = random.randint(0, 10)
                if y in check:
                    continue
                else:
                    check.append(y)
                    break

            Initword = word[y]
            InitwordMod = list(word[y])  # list != str

            random.shuffle(InitwordMod)  # permute les lettres de InitwordMod
            wordX = "".join(InitwordMod)
            wordX = str(wordX)

            os.system('clear')
            rep = Inside(score=Score, vie=Vie0, X=wordX)

            if rep == Initword:
                print("\nFélicitation ! Mot correct !\n")
                Score += 1
                time.sleep(2)
                # rep = input("Appuyer ENTRER pour continuer...\n")
                # if rep != None:
                #   continue
                continue
            elif rep != Initword:
                print("\nDommage !! Mot incorrect\n")
                Vie0 -= 1
                time.sleep(2)
                if Vie0 == 0:
                    print("\nGAME OVER !! Vous n'avez plus de vie restante !\n")
                    rep = input("Appuyer ENTRER pour revenir au menu principal.\n")
                    if rep != None:
                        break
                continue


    elif choix == 5:

        print("\nMERCI ET A LA PROCHAINE !!")
        break
