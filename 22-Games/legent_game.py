import os, time
import random


def createCharacter(name, type):
    return name + " " + type


def getHealth(dice1, dice2):
    health = (dice1 * dice2) / 2 + 10
    return health


def getStrenght(dice1, dice2):
    strenght = (dice1 * dice2) / 2 + 12
    return strenght


while True:

    print()

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 12)

    name = input("Name Your Legend :")
    type = input("Character Type (Human, Elf, Wiard, Orc, God):")

    legend1 = createCharacter(name, type)
    health1 = getHealth(dice1, dice2)
    strenght1 = getStrenght(dice1, dice2)

    print(legend1)
    print("HEALTH", health1)
    print("STRENGHT", strenght1)

    print()

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 12)

    name = input("Name Your Legend :")
    type = input("Character Type (Human, Elf, Wiard, Orc, God, Alien):")

    legend2 = createCharacter(name, type)
    health2 = getHealth(dice1, dice2)
    strenght2 = getStrenght(dice1, dice2)

    print(legend2)
    print("HEALTH", health2)
    print("STRENGTH", strenght2)

    diffStrength = abs(strenght1 - strenght2)
    roundCount = 0

    print("BATTLE TIME")
    print("The battle begins!")

    while True:
        roundCount += 1

        legend1RollNumber = dice6 = random.randint(1, 6)
        legend2RollNumber = dice6 = random.randint(1, 6)

        if legend1RollNumber > legend2RollNumber:
            health2 = health2 - diffStrength
            print(legend1, "wins the first blow")
            print(legend2, "takes a hit, with ", diffStrength, "damage")
            print()
            print(legend1)
            print("HEALTH", health1)
            print()
            print(legend2)
            print("HEALTH", health2)
        else:
            health1 = health1 - diffStrength
            print(legend2, "wins the first blow")
            print(legend1, "takes a hit, with ", diffStrength, "damage")
            print()
            print(legend2)
            print("HEALTH", health2)
            print()
            print(legend1)
            print("HEALTH", health1)

        if health1 <= 0:
            print("Oh no", legend1, "has died!")
            print()
            print(legend2, "destroyed", legend1, "in", roundCount, "rounds!")
            exit()
        elif health2 <= 0:
            print("Oh no", legend2, "has died!")
            print()
            print(legend1, "destroyed", legend2, "in", roundCount, "rounds!")
            exit()
        else:
            print("And they're both standing for the next round!")
            time.sleep(3)
            os.system("clear")







