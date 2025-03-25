"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Lukáš Bystroň
email: lbystron@gmail.com
"""
from time import time
from collections import Counter
import random

def welcome_user():
    '''uvitání hráče a představení hry'''
    print(f'''Hi there!\n{znak}\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.\n{znak}\nEnter a number:\n{znak}'''
    )

def random_number():
    ''' vygenerování náhodného čtyřmístného čísla
    a nesmí začínat 0
    '''
    return random.randint(1000, 9999)

def vyhodnoceni(uzi, pc, gg, cc):
    while pc != uzi:
        print(f"TEST: {pc}")
        try:
            uzi = int(input(">>> "))
            if len(str(uzi)) == 3:
                print("Číslo nesmí začínat číslem 0!")
            elif len(str(uzi)) != 4:
                print("Pouze čtyřciferné čísla!")
            else:
                print(f"{gg},{cc}")
        except ValueError:
            print("Pouze čísla!")
    print(f"{znak}\n>>> {pc}\nCorrect, you've guessed the right number\nin guesses!\n{znak}\nThat´s amazing!\nTime:")

def vyhodnoceni_bulls(PC, uzivatel):
    prevod_PC = list(map(int, str(PC)))
    prevod_uzi = list(map(int, str(uzivatel)))
    soucet_bulls = 0
    for i in range(len(prevod_PC)):
        if prevod_PC[int(i)] == prevod_uzi[int(i)]:
            soucet_bulls += 1
            zz.append("X")
        else:
            zz.append(i)
    if soucet_bulls == 1:
        return print(f"{soucet_bulls} bull, ")
    else:
        return print(f"{soucet_bulls} bulls, ")

def vyhodnoceni_cows(PC, uzivatel):
    rozdil = set(PC) & set(uzivatel)
    objekt = Counter(rozdil)
    soucet = sum(objekt.values())
    if soucet == 1:
        return print(f"{soucet} cow")
    else:
        return print(f"{soucet} cows")


znak = "-" * 47
welcome_user()
nahodne = random_number()
user = ()
vyhodnoceni(uzi=user, pc=nahodne, gg=vyhodnoceni_bulls, cc=vyhodnoceni_cows)
vyhodnoceni_bulls(PC=nahodne, uzivatel=user)
zz = []
vyhodnoceni_cows(PC=nahodne, uzivatel=zz)