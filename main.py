"""
TP2 | Jeu de devinettes
Nom: Noah Chamoiseau
Groupe: 4567
"""

import random

while True:
    nb_minimum = int(input("Choisissez le nombre minimum de l'ordinateur: "))
    nb_maximum = int(input("Choisissez le nombre maximum de l'ordinateur: "))
    nb_ordi = random.randint(nb_minimum, nb_maximum)
    nb_essai = 0

    print(f"J'ai choisi un nombre entre {nb_minimum} et {nb_maximum}. À vous de le deviner...")
    while True:
        essai = int(input("Entrez votre essai: "))
        nb_essai += 1
        if essai < nb_ordi:
            print(f"{essai} est plus petit que le nombre de l'ordinateur")
        elif essai > nb_ordi:
            print(f"{essai} est plus grand que le nombre de l'ordinateur")
        else:
            print(f"Bravo! Vous avez trouvez le nombre de l'ordianateur ({nb_ordi}) en {nb_essai} essai")
            break
    reponse = input("Voulez vouz rejouer? y/n\n")
    if reponse.lower() != "y":
        break
