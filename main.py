import random


class Character:
    def __init__(self, name, strength, attack, health, dexterity, chance):
        self.name = name
        self.strength = strength
        self.attack = attack
        self.health = health
        self.dexterity = dexterity
        self.chance = chance


class Chest:
    lock_difficulty = random.randint(1, 10)
    lock_chance = random.randint(1, 10)
    gold_pieces = random.randint(0, 10)


guerrier = Character
guerrier.name = 'Barbarian'
guerrier.strength = 10
guerrier.attack = 10
guerrier.health = 50
guerrier.dexterity = 2
guerrier.chance = 5

ennemi = Character
ennemi.name = 'Gobelin'
ennemi.strength = 10
ennemi.attack = 7
ennemi.health = 50


inventory = {"crochets": 5,
             "pièces d'or": 0,
             "potion": 0,
             "torche": 0,
             }


def ennemy_attack():
    damage = random.randint(0, ennemi.attack)
    print(f"L'ennemi inflige {damage} points de dégats.")
    print(f"Votre santé diminue à {guerrier.health - damage} points de vie.")


def display_gold_pieces():
    gp = inventory["pièces d'or"]
    print(f"Vous avez {gp} pièces d'or au total")


def chest():
    print(f"Vous trouvez un coffre fermé par une serrure de niveau {Chest.lock_difficulty} \n"
          f"(votre niveau de crochetage est de {guerrier.dexterity}). ")
    chest_answer = input("Voulez-vous tenter de l'ouvrir ? y/n : ")
    print()
    if chest_answer == "y":
        if guerrier.dexterity >= Chest.lock_difficulty and inventory["crochets"] > 1:
            print("Vous prenez des crochets et les introduisez dans la serrure.")
            print(f"Vous déverrouillez le coffre, il contient {Chest.gold_pieces} pièces d'or.")
            inventory["pièces d'or"] += Chest.gold_pieces
            display_gold_pieces()
        else:
            if guerrier.chance >= Chest.lock_chance:
                print("La serrure semble particulièrement difficle à ouvrir mais vous essayer quand même.")
                print(f"Avec un peu de patience et de chance vous réussissez à déverouiller le coffre."
                      f" Il contient {Chest.gold_pieces} pièces d'or.")
                inventory["pièces d'or"] += Chest.gold_pieces
                display_gold_pieces()
            else:
                print("Vous n'avez pas réussi à ouvrir le coffre.")
    if chest_answer == "n":
        print("Vous passez votre chemin")
