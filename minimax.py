from collections import Counter
import random
from main import format_code


def maximisation(choix, etat):
    evaluation_list = []
    for i in range(len(etat)):
        evaluation_list.append(valeur(choix, etat[i]))
    compteur_evaluation = Counter(evaluation_list).values()
    valeur_maximisation = max(compteur_evaluation)
    return valeur_maximisation


def valeur(choix, code):
    evaluation = sum((Counter(code) & Counter(choix)).values())
    val_juste = sum(i == j for i, j in zip(choix, code))
    reste = evaluation - val_juste
    return val_juste, reste


def mini_max(code, possibilite):
    colors = "RGBYWP"
    meilleur_choix = ""
    for i in range(0, 4):
        meilleur_choix += random.choice(colors)  # Choix d'une couleur arbitraire pour pouvoir correctement commencer l'élagage
    beta = len(possibilite)
    etat = possibilite
    tentative = 1
    while True:
        valeur_du_choix = valeur(meilleur_choix, code)
        print("\n")
        print("TENTATIVE N°{}: CHOIX DE L'IA : {}".format(tentative, format_code(meilleur_choix,code)))
        if meilleur_choix == code:
            print("PERDU ! L'IA A TROUVÉ LE CODE {} EN {} TENTATIVES".format(code, tentative))
            break
        etat = [i for i in etat if valeur(meilleur_choix, i) == valeur_du_choix]

        if len(etat) == 1:
            meilleur_choix = etat[0]
        else:
            for i in range(len(etat)):
                alpha = maximisation(etat[i], etat)
                if alpha < beta:
                    beta = alpha
                    meilleur_choix = etat[i]
                if etat[i] == code:
                    break

        tentative += 1
