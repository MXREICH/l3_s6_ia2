from colorama import Fore, Back
from err import err
import random
import time


def format_code(essai, code):
    res = essai
    check = ""
    for i in range(len(essai)):  # Vérification des coups
        if code[i] == essai[i]:
            res += " " +Back.LIGHTGREEN_EX + Fore.BLACK + "[✓]" + Back.RESET + Fore.RESET
            check += essai[i]

    for i in range(len(essai)):
        if essai[i] in code and code[i] != essai[i] and essai[i] not in check:
            res += " "+Back.LIGHTYELLOW_EX + Fore.BLACK + "[⁓]" + Back.RESET + Fore.RESET

    for i in range(len(essai)):
        if essai[i] not in code:
            res += " "+Back.LIGHTRED_EX + Fore.BLACK + "[✕]" + Back.RESET + Fore.RESET
    res += "\n"
    return res


def partie_joueur():
    # Génération aléatoire d'un code pour que le joueur puisse décoder:
    colors = 'RBYGWP'
    code = ""
    for i in range(0, 4):
        code += random.choice(colors)
    anciens = ""
    tentative = 0
    partie = True

    while partie:
        print("\n" * 100)
        print("\nTENTATIVES PASSÉES:")
        print(anciens)
        print("COULEURS POSSIBLES: {}".format(colors))
        essai = input("TENTATIVE N°{}: ".format(tentative + 1)).upper()
        if len(essai) != len(code):  # Vérification pour la longueur du code
            err("CODE DE LONGUEUR INVALIDE")
        for i in range(len(essai)):  # Vérification de validité de couleur
            if essai[i] not in colors:
                err("{} N'EST PAS UNE COULEUR POSSIBLE".format(essai[i]))
        if essai == code:  # Réussite
            print("BRAVO ! VOUS AVEZ BREAK EN {} TENTATIVES !".format(tentative + 1))
            print(anciens)
            break
        if tentative > 10:  # Échec
            err("LE BON CODE ÉTAIT: {}.".format(code))
        tentative += 1
        anciens += format_code(essai, code)


def partie_ia():
    colors = 'LOL'

"""
La fonction create_code vérifie que le joueur a bien entré un code
égal à quatre couleurs et que les couleurs sont bien celles demandées
"""
def create_code():
    valid_color = 'RGBYWP'
    demande = input("Veuillez entrer un code de 4 couleurs parmi RGBYWP: ")

    # Vérifier que le code est de bonne longueur
    if len(demande) != 4:
        err("CODE DONNÉ EST DE MAUVAISE LONGUEUR")


    # Vérifier que chaque couleur est valide
    for couleur in demande:
        if couleur not in valid_color:
            err("COULEUR DONNÉE NON VALIDE")

    return demande

def game_rules(choix):
    if choix == 1:
        print("\t\t\t\t\t\t\t\tC'est à vous de choisir un code ! .\n\t\t\tLes couleurs sont: " + Fore.RED +
              "rouge(R), " + Fore.GREEN + "vert(G), " + Fore.BLUE + "bleu(B), " + Fore.YELLOW + "jaune(Y), "
              + Fore.WHITE + "blanc(W), " + Fore.MAGENTA + "violet(P)" + Fore.RESET)
        print("\t\t\t\t\t\t\t\tUn bon exemple de code à créer serait: RGBW")
        print("\t\t\t\t\tÀ chaque envoi d'une réponse par l'ia, il vous sera montré quatre jetons.")
    if choix == 2:
        print("\t\t\t\t\t\t\t\tC'est à vous de deviner un code ! .\n\t\t\tLes couleurs sont: " + Fore.RED +
              "rouge(R), " + Fore.GREEN + "vert(G), " + Fore.BLUE + "bleu(B), " + Fore.YELLOW + "jaune(Y), "
              + Fore.WHITE + "blanc(W), " + Fore.MAGENTA + "violet(P)" + Fore.RESET)
        print("\t\t\t\t\t\t\t\tUn bon exemple à deviner serait: RGBW")
        print("\t\t\t\t\tÀ chaque envoi d'une de vos réponse, il vous sera montré quatre jetons.")

    print("\t\t\tLe jeton " + Back.LIGHTGREEN_EX + Fore.BLACK + "[✓]" + Back.RESET + Fore.RESET + " signifie"
          " qu'un des choix est de la bonne couleur au bon endroit")
    print("\t\t  Le jeton " + Back.LIGHTYELLOW_EX + Fore.BLACK + "[⁓]" + Back.RESET + Fore.RESET + " signifie"
          " qu'un des choix est de la bonne couleur au mauvais endroit")
    print("\t\t\t\tLe jeton " + Back.LIGHTRED_EX + Fore.BLACK + "[✕]" + Back.RESET + Fore.RESET + " signifie"
          " qu'un des choix n'est pas une couleur du code")
    time.sleep(10)


def main():
    print("\n" * 100)
    print("\t\t\t\t\t\t\t\t+====================================================+")
    print("\t\t\t\t\t\t\t\t|                     MASTERMIND                     |")
    print("\t\t\t\t\t\t\t\t+====================================================+")
    print("\t\t\t\t\t\t Les règles sont simples, devinez un code en faisant le moins d'essai")
    choix = input(
        "\t\t\t\t\t\t\t\t  Choisissez " + Back.LIGHTRED_EX + Fore.BLACK + "1" + Back.RESET + Fore.RESET + " pour "
                                                                                                          "choisir un "
                                                                                                          "code ou "
        + Back.LIGHTBLUE_EX + Fore.BLACK + "2" + Back.RESET + Fore.RESET + " pour jouer au jeu: \n\n\n\n\n")
    print("\n" * 100)
    if choix == '1':
        game_rules(1)
        joueur_breaker = False
    elif choix == '2':
        game_rules(2)
        joueur_breaker = True
    else:
        err("CHOISISSEZ 1 OU 2")
    if joueur_breaker:
        partie_joueur()
    else:
        partie_ia()


if __name__ == "__main__":
    main()
