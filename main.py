"""
TP2 | Jeu de devinettes
Nom: Noah Chamoiseau
Groupe: 4567
"""

import random

def choix_bornes ():
    changer_bornes = input("Voulez-vous changer les bornes de l'ordinateur (0, 100) (o/n)? ")
    if changer_bornes.lower() == "o":
        borne_min = int(input("Choisissez le nombre minimum de l'ordinateur: "))
        borne_max = int(input("Choisissez le nombre maximum de l'ordinateur: "))
        return borne_min, borne_max
    else:
        return 0, 100

while True:
    nb_minimum, nb_maximum = choix_bornes()
    nb_ordi = random.randint(nb_minimum, nb_maximum)
    nb_essais = 0

    print(f"J'ai choisi un nombre entre {nb_minimum} et {nb_maximum}. À vous de le deviner...")
    while True:
        essai = int(input("Entrez votre essai: "))
        nb_essais += 1
        if essai < nb_ordi:
            print(f"{essai} est plus petit que le nombre de l'ordinateur")
        elif essai > nb_ordi:
            print(f"{essai} est plus grand que le nombre de l'ordinateur")
        else:
            print(f"Bravo! Bonne réponse\nVous avez réussi en : {nb_essais} essai(s)")
            break
    reponse = input("Voulez-vouz faire une autre partie (o/n)? ")
    if reponse.lower() != "o":
        print("Merci et au revoir...")
        break

